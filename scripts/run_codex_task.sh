#!/bin/bash
# scripts/run_codex_task.sh — Claude Code → Codex 委譲 wrapper
#
# Usage:
#   bash scripts/run_codex_task.sh analyze "質問・指示文"
#   bash scripts/run_codex_task.sh analyze --prompt-file path/to/prompt.txt
#   CODEX_APPLY_ALLOWED=1 bash scripts/run_codex_task.sh apply "修正指示文"
#
# 環境変数（オーバーライド用）:
#   CODEX_CMD             codex バイナリのパス（デフォルト: codex）
#   CODEX_ANALYZE_FLAGS   analyze モードの追加フラグ
#   CODEX_APPLY_FLAGS     apply モードの追加フラグ
#
# 参照: docs/CODEX_DELEGATION.md

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$REPO_ROOT/logs/codex"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

# codex コマンド（環境変数でオーバーライド可能）
CODEX_CMD="${CODEX_CMD:-codex}"

# モード確認
MODE="${1:?Error: mode required (analyze|apply)}"
shift

if [[ "$MODE" != "analyze" && "$MODE" != "apply" ]]; then
  echo "Error: mode must be 'analyze' or 'apply' (got: $MODE)"
  exit 1
fi

# apply 安全弁
if [[ "$MODE" == "apply" && "${CODEX_APPLY_ALLOWED:-}" != "1" ]]; then
  echo "Error: apply mode requires CODEX_APPLY_ALLOWED=1"
  echo "Usage: CODEX_APPLY_ALLOWED=1 bash scripts/run_codex_task.sh apply \"prompt\""
  exit 1
fi

# プロンプト解決（inline or --prompt-file）
PROMPT=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt-file)
      if [[ -z "${2:-}" ]]; then
        echo "Error: --prompt-file requires a file path"
        exit 1
      fi
      PROMPT="$(cat "$2")"
      shift 2
      ;;
    *)
      PROMPT="$1"
      shift
      ;;
  esac
done

if [[ -z "$PROMPT" ]]; then
  echo "Error: prompt is empty"
  echo "Usage: bash scripts/run_codex_task.sh analyze \"prompt\""
  exit 1
fi

# codex インストール確認
if ! command -v "$CODEX_CMD" &>/dev/null; then
  echo "Error: codex not found (CODEX_CMD=$CODEX_CMD)"
  echo "Install codex or set CODEX_CMD to the correct path."
  exit 1
fi

mkdir -p "$LOG_DIR"
EVT_FILE="$LOG_DIR/${TIMESTAMP}_${MODE}_events.log"
EXIT_CODE=0

cd "$REPO_ROOT"

if [[ "$MODE" == "analyze" ]]; then
  MSG_FILE="$LOG_DIR/${TIMESTAMP}_${MODE}_message.json"
  # read-only: --json で event log を stdout 出力、-o で最終メッセージを保存
  # analyze は --sandbox read-only をデフォルトとする
  EXTRA_FLAGS="${CODEX_ANALYZE_FLAGS:-}"
  # shellcheck disable=SC2086
  "$CODEX_CMD" exec --json -o "$MSG_FILE" -s read-only $EXTRA_FLAGS "$PROMPT" \
    > "$EVT_FILE" 2>&1 || EXIT_CODE=$?

  echo "exit_code=$EXIT_CODE" >> "$EVT_FILE"

  if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[FAILED] exit=$EXIT_CODE"
    echo "  events log: $EVT_FILE"
    exit $EXIT_CODE
  fi
  echo "[OK] mode=analyze"
  echo "  events log: $EVT_FILE"
  echo "  message:    $MSG_FILE"

else
  # apply: --full-auto は workspace-write sandbox で自動実行
  EXTRA_FLAGS="${CODEX_APPLY_FLAGS:-}"
  # shellcheck disable=SC2086
  "$CODEX_CMD" exec --full-auto $EXTRA_FLAGS "$PROMPT" \
    > "$EVT_FILE" 2>&1 || EXIT_CODE=$?

  echo "exit_code=$EXIT_CODE" >> "$EVT_FILE"

  if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[FAILED] exit=$EXIT_CODE"
    echo "  events log: $EVT_FILE"
    exit $EXIT_CODE
  fi
  echo "[OK] mode=apply"
  echo "  events log: $EVT_FILE"
  echo ""
  echo "--- apply 完了。必ず git diff --stat で変更内容を確認してください ---"
  echo "  git diff --stat"
  echo "  git diff          # 詳細確認が必要な場合"
  echo "  git checkout -- . # 問題があれば差し戻し"
fi
