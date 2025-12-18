# main.py
# Đề tài 4: Kiểm tra số đối xứng (Palindrome)
# Lớp: 25CT114 ; Nhóm: 16

def dao_nguoc_so(n: int) -> int:
    so_dao = 0
    tam = n
    while tam > 0:
        chu_so = tam % 10
        so_dao = so_dao * 10 + chu_so
        tam //= 10
    return so_dao

def la_so_doi_xung(n: int) -> bool:
    return n == dao_nguoc_so(n)

def tong_cac_so_doi_xung(a: int, b: int) -> int:
    tong = 0
    for i in range(a, b + 1):
        if la_so_doi_xung(i):
            tong += i
    return tong

def liet_ke_cac_so_doi_xung(a: int, b: int) -> list[int]:
    danh_sach = []
    for i in range(a, b + 1):
        if la_so_doi_xung(i):
            danh_sach.append(i)
    return danh_sach

def nhap_so_nguyen_duong(thong_bao: str) -> int:
    while True:
        try:
            gia_tri = int(input(thong_bao))
            if gia_tri <= 0:
                print("❌ Vui lòng nhập số nguyên dương (> 0).")
                continue
            return gia_tri
        except ValueError:
            print("❌ Dữ liệu không hợp lệ. Hãy nhập MỘT SỐ NGUYÊN (ví dụ: 7, 121).")

def nhap_lua_chon_menu() -> int:
    while True:
        try:
            lua_chon = int(input("Chọn chức năng (0-3): "))
            if lua_chon in (0, 1, 2, 3):
                return lua_chon
            print("❌ Chỉ được chọn 0, 1, 2 hoặc 3. Vui lòng chọn lại.")
        except ValueError:
            print("❌ Vui lòng nhập số nguyên 0, 1, 2 hoặc 3.")

def chuan_hoa_doan(a: int, b: int) -> tuple[int, int]:
    if a > b:
        print("⚠️ Bạn nhập A > B. Chương trình sẽ tự hoán đổi để tính trong đoạn [B, A].")
        a, b = b, a
    return a, b

def main():
    print("======================================")
    print("ĐỀ TÀI 4 - KIỂM TRA SỐ ĐỐI XỨNG (PALINDROME)")
    print("Nhóm 16 – Đề tài số 4.")
    print("======================================")

    while True:
        print("\n----- MENU -----")
        print("1) Kiểm tra một số có phải số đối xứng")
        print("2) Tính tổng các số đối xứng trong đoạn [A, B]")
        print("3) Liệt kê các số đối xứng trong đoạn [N, M]")
        print("0) Thoát")

        lua_chon = nhap_lua_chon_menu()

        if lua_chon == 0:
            print("✅ Kết thúc chương trình. Tạm biệt!")
            break

        if lua_chon == 1:
            n = nhap_so_nguyen_duong("Nhập số nguyên dương n: ")
            if la_so_doi_xung(n):
                print(f"✅ {n} là số đối xứng.")
            else:
                print(f"❌ {n} không phải số đối xứng.")

        elif lua_chon == 2:
            a = nhap_so_nguyen_duong("Nhập số nguyên dương A: ")
            b = nhap_so_nguyen_duong("Nhập số nguyên dương B: ")
            a, b = chuan_hoa_doan(a, b)

            tong = tong_cac_so_doi_xung(a, b)
            print(f"✅ Tổng các số đối xứng trong đoạn [{a}, {b}] là: {tong}")

        elif lua_chon == 3:
            n = nhap_so_nguyen_duong("Nhập số nguyên dương N: ")
            m = nhap_so_nguyen_duong("Nhập số nguyên dương M: ")
            n, m = chuan_hoa_doan(n, m)

            ds = liet_ke_cac_so_doi_xung(n, m)
            if ds:
                print(f"✅ Các số đối xứng trong đoạn [{n}, {m}] là:")
                print(*ds, sep=", ")
                print(f"➡️ Có tất cả {len(ds)} số đối xứng.")
            else:
                print(f"⚠️ Không có số đối xứng nào trong đoạn [{n}, {m}].")

if __name__ == "__main__":
    main()
