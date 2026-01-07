from src.web.online_viewer import OnlineViewer

def main():
    ov = OnlineViewer()
    url = ov.view_profile("instagram")
    print("Opened:", url)

if __name__ == "__main__":
    main()
