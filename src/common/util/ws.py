async def handle_playbook_result(process, websocket):
    for line in iter(process.stdout.readline, ""):
        await websocket.send_text(line)
    process.stdout.close()
    process.wait()
    await websocket.send_text("本次任务执行结束.")
