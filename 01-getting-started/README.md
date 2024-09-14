# Goals of this document

I tried to use `wireshark` and got the packet for hands-on website `http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html`. But I can not get the packet from it using wireshark. Filtered the related network transaction like `tcp.srcport == 80` but I can not get the result that I want.

So, I decided to create a container environment for running runtime-agnostic hands-on.

**If someone look this repository for hands on the labs of computer network: top down approach, please help me.**

# Prerequisites

- container runtime, I used docker.

# Command

```shell
docker build -t tcpdump-capture-container . && \
docker run --rm -it \
  --net=host \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  tcpdump-capture-container
```

# Result

```shell
Analyzing the captured packets...
13 packets captured
13 packets received by filter
0 packets dropped by kernel
reading from file /tmp/output.pcap, link-type EN10MB (Ethernet), snapshot length 262144
16:10:28.544049 IP (tos 0x0, ttl 64, id 825, offset 0, flags [DF], proto TCP (6), length 60)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [S], cksum 0x34c9 (incorrect -> 0x2e11), seq 1253745889, win 64240, options [mss 1460,sackOK,TS val 2004073693 ecr 0,nop,wscale 7], length 0
        0x0000:  4500 003c 0339 4000 4006 02e9 c613 f902  E..<.9@.@.......
        0x0010:  8077 f50c c626 0050 4aba a4e1 0000 0000  .w...&.PJ.......
        0x0020:  a002 faf0 34c9 0000 0204 05b4 0402 080a  ....4...........
        0x0030:  7773 bcdd 0000 0000 0103 0307            ws..........
16:10:29.306466 IP (tos 0x0, ttl 63, id 18011, offset 0, flags [none], proto TCP (6), length 60)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [S.], cksum 0xfeff (incorrect -> 0x0f7a), seq 3626582876, ack 1253745890, win 65408, options [mss 65479,nop,nop,TS val 534833020 ecr 2004073693,nop,wscale 7], length 0
        0x0000:  4500 003c 465b 0000 3f06 00c7 8077 f50c  E..<F[..?....w..
        0x0010:  c613 f902 0050 c626 d829 435c 4aba a4e2  .....P.&.)C\J...
        0x0020:  a012 ff80 feff 0000 0204 ffc7 0101 080a  ................
        0x0030:  1fe0 e77c 7773 bcdd 0103 0307            ...|ws......
16:10:29.306604 IP (tos 0x0, ttl 64, id 826, offset 0, flags [DF], proto TCP (6), length 52)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [.], cksum 0x34c1 (incorrect -> 0x2fea), seq 1, ack 1, win 502, options [nop,nop,TS val 2004074455 ecr 534833020], length 0
        0x0000:  4500 0034 033a 4000 4006 02f0 c613 f902  E..4.:@.@.......
        0x0010:  8077 f50c c626 0050 4aba a4e2 d829 435d  .w...&.PJ....)C]
        0x0020:  8010 01f6 34c1 0000 0101 080a 7773 bfd7  ....4.......ws..
        0x0030:  1fe0 e77c                                ...|
16:10:29.306983 IP (tos 0x0, ttl 64, id 827, offset 0, flags [DF], proto TCP (6), length 173)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [P.], cksum 0x353a (incorrect -> 0x9f68), seq 1:122, ack 1, win 502, options [nop,nop,TS val 2004074456 ecr 534833020], length 121: HTTP, length: 121
        GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1
        Host: gaia.cs.umass.edu
        User-Agent: curl/8.5.0
        Accept: */*

        0x0000:  4500 00ad 033b 4000 4006 0276 c613 f902  E....;@.@..v....
        0x0010:  8077 f50c c626 0050 4aba a4e2 d829 435d  .w...&.PJ....)C]
        0x0020:  8018 01f6 353a 0000 0101 080a 7773 bfd8  ....5:......ws..
        0x0030:  1fe0 e77c 4745 5420 2f77 6972 6573 6861  ...|GET./wiresha
        0x0040:  726b 2d6c 6162 732f 494e 5452 4f2d 7769  rk-labs/INTRO-wi
        0x0050:  7265 7368 6172 6b2d 6669 6c65 312e 6874  reshark-file1.ht
        0x0060:  6d6c 2048 5454 502f 312e 310d 0a48 6f73  ml.HTTP/1.1..Hos
        0x0070:  743a 2067 6169 612e 6373 2e75 6d61 7373  t:.gaia.cs.umass
        0x0080:  2e65 6475 0d0a 5573 6572 2d41 6765 6e74  .edu..User-Agent
        0x0090:  3a20 6375 726c 2f38 2e35 2e30 0d0a 4163  :.curl/8.5.0..Ac
        0x00a0:  6365 7074 3a20 2a2f 2a0d 0a0d 0a         cept:.*/*....
16:10:29.307071 IP (tos 0x0, ttl 63, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [.], cksum 0x34c1 (incorrect -> 0x2f68), seq 1, ack 122, win 510, options [nop,nop,TS val 534833020 ecr 2004074456], length 0
        0x0000:  4500 0034 0000 4000 3f06 072a 8077 f50c  E..4..@.?..*.w..
        0x0010:  c613 f902 0050 c626 d829 435d 4aba a55b  .....P.&.)C]J..[
        0x0020:  8010 01fe 34c1 0000 0101 080a 1fe0 e77c  ....4..........|
        0x0030:  7773 bfd8                                ws..
16:10:29.592748 IP (tos 0x0, ttl 63, id 0, offset 0, flags [DF], proto TCP (6), length 434)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [P.], cksum 0x363f (incorrect -> 0x39ce), seq 1:383, ack 122, win 4096, options [nop,nop,TS val 534833306 ecr 2004074456], length 382: HTTP, length: 382
        HTTP/1.1 200 OK
        Date: Sat, 14 Sep 2024 16:10:29 GMT
        Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.33 mod_perl/2.0.11 Perl/v5.16.3
        Last-Modified: Sat, 14 Sep 2024 05:59:01 GMT
        ETag: "51-6220e09566130"
        Accept-Ranges: bytes
        Content-Length: 81
        Content-Type: text/html; charset=UTF-8

        <html>
        Congratulations!  You've downloaded the first Wireshark lab file!
        </html>
        0x0000:  4500 01b2 0000 4000 3f06 05ac 8077 f50c  E.....@.?....w..
        0x0010:  c613 f902 0050 c626 d829 435d 4aba a55b  .....P.&.)C]J..[
        0x0020:  8018 1000 363f 0000 0101 080a 1fe0 e89a  ....6?..........
        0x0030:  7773 bfd8 4854 5450 2f31 2e31 2032 3030  ws..HTTP/1.1.200
        0x0040:  204f 4b0d 0a44 6174 653a 2053 6174 2c20  .OK..Date:.Sat,.
        0x0050:  3134 2053 6570 2032 3032 3420 3136 3a31  14.Sep.2024.16:1
        0x0060:  303a 3239 2047 4d54 0d0a 5365 7276 6572  0:29.GMT..Server
        0x0070:  3a20 4170 6163 6865 2f32 2e34 2e36 2028  :.Apache/2.4.6.(
        0x0080:  4365 6e74 4f53 2920 4f70 656e 5353 4c2f  CentOS).OpenSSL/
        0x0090:  312e 302e 326b 2d66 6970 7320 5048 502f  1.0.2k-fips.PHP/
        0x00a0:  372e 342e 3333 206d 6f64 5f70 6572 6c2f  7.4.33.mod_perl/
        0x00b0:  322e 302e 3131 2050 6572 6c2f 7635 2e31  2.0.11.Perl/v5.1
        0x00c0:  362e 330d 0a4c 6173 742d 4d6f 6469 6669  6.3..Last-Modifi
        0x00d0:  6564 3a20 5361 742c 2031 3420 5365 7020  ed:.Sat,.14.Sep.
        0x00e0:  3230 3234 2030 353a 3539 3a30 3120 474d  2024.05:59:01.GM
        0x00f0:  540d 0a45 5461 673a 2022 3531 2d36 3232  T..ETag:."51-622
        0x0100:  3065 3039 3536 3631 3330 220d 0a41 6363  0e09566130"..Acc
        0x0110:  6570 742d 5261 6e67 6573 3a20 6279 7465  ept-Ranges:.byte
        0x0120:  730d 0a43 6f6e 7465 6e74 2d4c 656e 6774  s..Content-Lengt
        0x0130:  683a 2038 310d 0a43 6f6e 7465 6e74 2d54  h:.81..Content-T
        0x0140:  7970 653a 2074 6578 742f 6874 6d6c 3b20  ype:.text/html;.
        0x0150:  6368 6172 7365 743d 5554 462d 380d 0a0d  charset=UTF-8...
        0x0160:  0a3c 6874 6d6c 3e0a 436f 6e67 7261 7475  .<html>.Congratu
        0x0170:  6c61 7469 6f6e 7321 2020 596f 7527 7665  lations!..You've
        0x0180:  2064 6f77 6e6c 6f61 6465 6420 7468 6520  .downloaded.the.
        0x0190:  6669 7273 7420 5769 7265 7368 6172 6b20  first.Wireshark.
        0x01a0:  6c61 6220 6669 6c65 210a 3c2f 6874 6d6c  lab.file!.</html
        0x01b0:  3e0a                                     >.
16:10:29.592820 IP (tos 0x0, ttl 64, id 828, offset 0, flags [DF], proto TCP (6), length 52)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [.], cksum 0x34c1 (incorrect -> 0x2bb9), seq 122, ack 383, win 500, options [nop,nop,TS val 2004074741 ecr 534833306], length 0
        0x0000:  4500 0034 033c 4000 4006 02ee c613 f902  E..4.<@.@.......
        0x0010:  8077 f50c c626 0050 4aba a55b d829 44db  .w...&.PJ..[.)D.
        0x0020:  8010 01f4 34c1 0000 0101 080a 7773 c0f5  ....4.......ws..
        0x0030:  1fe0 e89a                                ....
16:10:29.593320 IP (tos 0x0, ttl 64, id 829, offset 0, flags [DF], proto TCP (6), length 52)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [F.], cksum 0x34c1 (incorrect -> 0x2bb6), seq 122, ack 383, win 501, options [nop,nop,TS val 2004074742 ecr 534833306], length 0
        0x0000:  4500 0034 033d 4000 4006 02ed c613 f902  E..4.=@.@.......
        0x0010:  8077 f50c c626 0050 4aba a55b d829 44db  .w...&.PJ..[.)D.
        0x0020:  8011 01f5 34c1 0000 0101 080a 7773 c0f6  ....4.......ws..
        0x0030:  1fe0 e89a                                ....
16:10:29.593511 IP (tos 0x0, ttl 63, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [.], cksum 0x34c1 (incorrect -> 0x1dac), seq 383, ack 123, win 4095, options [nop,nop,TS val 534833307 ecr 2004074741], length 0
        0x0000:  4500 0034 0000 4000 3f06 072a 8077 f50c  E..4..@.?..*.w..
        0x0010:  c613 f902 0050 c626 d829 44db 4aba a55c  .....P.&.)D.J..\
        0x0020:  8010 0fff 34c1 0000 0101 080a 1fe0 e89b  ....4...........
        0x0030:  7773 c0f5                                ws..
16:10:29.595374 IP (tos 0x0, ttl 63, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [F.], cksum 0x34c1 (incorrect -> 0x1da8), seq 383, ack 123, win 4096, options [nop,nop,TS val 534833308 ecr 2004074742], length 0
        0x0000:  4500 0034 0000 4000 3f06 072a 8077 f50c  E..4..@.?..*.w..
        0x0010:  c613 f902 0050 c626 d829 44db 4aba a55c  .....P.&.)D.J..\
        0x0020:  8011 1000 34c1 0000 0101 080a 1fe0 e89c  ....4...........
        0x0030:  7773 c0f6                                ws..
16:10:29.595420 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    198.19.249.2.50726 > gaia.cs.umass.edu.80: Flags [.], cksum 0x2bb1 (correct), seq 123, ack 384, win 501, options [nop,nop,TS val 2004074744 ecr 534833308], length 0
        0x0000:  4500 0034 0000 4000 4006 062a c613 f902  E..4..@.@..*....
        0x0010:  8077 f50c c626 0050 4aba a55c d829 44dc  .w...&.PJ..\.)D.
        0x0020:  8010 01f5 2bb1 0000 0101 080a 7773 c0f8  ....+.......ws..
        0x0030:  1fe0 e89c                                ....
16:10:29.595376 IP (tos 0x0, ttl 63, id 0, offset 0, flags [DF], proto TCP (6), length 52)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [R.], cksum 0x34c1 (incorrect -> 0x2da4), seq 384, ack 123, win 0, options [nop,nop,TS val 534833308 ecr 2004074742], length 0
        0x0000:  4500 0034 0000 4000 3f06 072a 8077 f50c  E..4..@.?..*.w..
        0x0010:  c613 f902 0050 c626 d829 44dc 4aba a55c  .....P.&.)D.J..\
        0x0020:  8014 0000 34c1 0000 0101 080a 1fe0 e89c  ....4...........
        0x0030:  7773 c0f6                                ws..
16:10:29.596589 IP (tos 0x0, ttl 63, id 65476, offset 0, flags [none], proto TCP (6), length 40)
    gaia.cs.umass.edu.80 > 198.19.249.2.50726: Flags [R], cksum 0xfeff (incorrect -> 0x97c9), seq 3626583260, win 0, length 0
        0x0000:  4500 0028 ffc4 0000 3f06 4771 8077 f50c  E..(....?.Gq.w..
        0x0010:  c613 f902 0050 c626 d829 44dc 0000 0000  .....P.&.)D.....
        0x0020:  5004 0000 feff 0000                      P.......
Packet capture and analysis complete!
```
