def cau_hoi(name):
    diem = 0
    truoc = ""
    sau = ""
    cau_so = 1
    while cau_so <= 10:
        # Thực hiện câu hỏi
        cau_hoi = ""
        if cau_so == 1:
            cau_hoi = "Năm 2020 chiếc máy console next gen của Playstation có tên là gì ?\n a. Playstation 5\n b. Ps5\n c. Playstation 4\n d. Ps Vita\n"
            cau_dung = "a"
        elif cau_so == 2:
            cau_hoi = "Chiếc máy trên thuộc thế hệ thứ mấy của console ?\n a. Thế hệ thứ 1\n b. Thé hệ thứ 5\n c. Thế hệ thứ 9\n d. Thế hệ thứ 7\n"
            cau_dung = "c"
        elif cau_so == 3:
            cau_hoi = "Chiếc máy handheld nổi tiếng nhất hiện nay với khả năng chơi mọi tựa game mà nó được hỗ trợ tên gì ?\n a. Steam deck\n b. Rog Ally\n c. Nintendo switch\n d. Ps Portal\n"
            cau_dung = "c"
        elif cau_so == 4:
            cau_hoi = "Chiếc điện thoại mới ra mắt gần đây và được giới thiệu có thể chơi game AAA (game đồ họa cao) tên gì ?\n a. Iphone 15\n b. Red magic\n c. Black shark\n d. Samsung\n"
            cau_dung = "a"
        elif cau_so == 5:
            cau_hoi = "Nintendo có lịch sử lâu đời và xuất phát với ngành gì ?\n a. Thiết kế Game\n b. Thiết kế máy chơi game\n c. Thiết kế đồ chơi\n d. Thiết kế máy nghe nhạc\n" 
            cau_dung = "c"
        elif cau_so == 6:
            cau_hoi = "Nintendo đã phát triển và tồn tại được bao nhiêu năm ?\n a. <= 100 năm\n b. >= 100 năm\n c. >= 50 năm\n d. ≈ 50 năm\n"
            cau_dung = "b"
        elif cau_so == 7:
            cau_hoi = "Playstation là gì 1 nhánh của công ty công nghệ nào ?\n a. Microsoft\n b. Sony\n c. Xbox\n d. Asus\n"
            cau_dung = "b"
        elif cau_so == 8:
            cau_hoi = "Sony và Nintendo có trụ sở ở đâu ?\n a. Mỹ\n b. Nhật bản\n c. Hàn Quốc\n d. Canada\n"
            cau_dung = "b"
        elif cau_so == 9:
            cau_hoi = "Sony đã phát triển công nghệ mới cho tay cầm của họ và tên nó là gì ?\n a. Dualsense\n b. Dualsock\n c. Controller\n d. DareU\n"
            cau_dung = "a"
        elif cau_so == 10:
            cau_hoi = "Tay cầm của họ đã phát triển công nghệ gì ? a. Haptic feedback\n b. Adaptive trigger\n c. a và b sai\n d. a và b đúng \n"
            cau_dung = "d"
        # Tương tự cho các câu hỏi khác

        cau_tra_loi = input(f"Câu {cau_so}: {cau_hoi}")
        if cau_tra_loi.lower() == cau_dung or cau_tra_loi.lower() in cau_dung:
            print("Đúng")
            if cau_so % 2 == 0:
                diem += 200
            else:
                diem +=100
        else:
            print("Sai")
            break
        
        # Chuyển sang câu hỏi tiếp theo hoặc kết thúc chương trình
        cau_so += 1
    
    print(f"Điểm của bạn là: {diem}")

name = input("Nhập tên của bạn: ").lower()
cau_hoi(name)
