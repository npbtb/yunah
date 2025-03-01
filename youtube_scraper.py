import yt_dlp

# 1️⃣ 用户输入 YouTube 播放列表 URL
playlist_url = input("请输入 YouTube 播放列表 URL: ")

try:
    # 2️⃣ 设置 yt-dlp 参数，提取播放列表信息
    ydl_opts = {
        'quiet': True,  # 静默模式
        'extract_flat': True,  # 只解析，不下载
        'force_generic_extractor': True,  # 强制使用通用解析器
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        
        print(f"\n🎥 找到 {len(info['entries'])} 个视频:\n")
        
        # 3️⃣ 遍历播放列表，输出标题和链接
        for index, video in enumerate(info['entries'], start=1):
            print(f"{index}. {video['title']} - {video['url']}")

except Exception as e:
    print(f"\n❌ 发生错误: {e}")

