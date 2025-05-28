monhoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thutu = [2, 3, 4, 1]
diemso = [10, 9, 8, 7]

anhxa = list(zip(thutu, monhoc, diemso))
anhxa.sort()

for thutu, monhoc, diemso in anhxa: 
    print(f"Thu tu {thutu}: Mon {monhoc} - Diem {diemso}")
