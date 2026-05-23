# Pretrained weights

Đặt file `pvt_v2_b2.pth` vào thư mục này trước khi train.

## Tải về

Từ repo PVTv2 chính chủ (https://github.com/whai362/PVT):

```bash
wget https://github.com/whai362/PVT/releases/download/v2/pvt_v2_b2.pth -O pvt_v2_b2.pth
```

Hoặc tải trực tiếp file `pvt_v2_b2.pth` (~89 MB) từ trang Releases của repo trên rồi copy vào đây.

Path tham chiếu trong config: `/root/haidm/pest-pvt-haidm/pretrained/pvt_v2_b2.pth`
(xem `configs/atss_pvtv2_dyhead3_ass.py`, key `pretrained=...`)