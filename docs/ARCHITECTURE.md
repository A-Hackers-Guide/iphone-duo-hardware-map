# Architecture at a glance

One picture of the Duo's SoC and the parts around it, built only from what the chapters and generated maps establish. Every box names its device-tree node; follow the links below the diagram for the evidence. Dashed boxes are Duo-only hardware ([09](09-what-makes-it-a-duo.md)).

```mermaid
flowchart LR
  subgraph SOC["t8160 / A20 Pro SoC"]
    direction TB
    subgraph CPU["CPU: 4 E-cores (sawtooth) + 2 P-cores (everest)"]
      XNU["XNU kernel<br/>322 kexts"]
      SPTM["SPTM / TXM<br/>page-table and code-signing monitors"]
      CL4["cL4 exclaves"]
    end
    AIC["AIC v3<br/>/arm-io/aic"]
    PMGR["PMGR power/clock<br/>/arm-io/pmgr"]
    MCC["AMCC / DCS<br/>memory controller"]
    GPU["AGX G19P GPU<br/>/arm-io/sgx"]
    GFX["gfx-asc + gfx1-asc<br/>GPU firmware cores"]
    ANE["ANE0 + ANE1<br/>/arm-io/ane0, ane1"]
    ISP["ISP<br/>/arm-io/ispRtb"]
    AVE["AVE encoder (RISC-V slices)<br/>AVD decoder, JPEG, scaler"]
    DCP["DCP → disp0<br/>outer panel"]
    DCPSEC["DCPSEC → dispsec<br/>inner panel"]:::duo
    DCPEXT["DCPEXT → USB-C DisplayPort"]
    AOP["AOP<br/>sensors, audio, voice trigger"]
    AOP2["AOP2<br/>always-on networking, GNSS"]
    MTP["MTP<br/>multitouch co-processor"]
    SMC["SMC<br/>PMU, charger, buttons"]
    PMP["PMP<br/>power manager"]
    ANS["ANS2<br/>NVMe controller"]
    SEP["SEP<br/>Secure Enclave"]
    SIO["SIO<br/>Smart I/O DMA"]
    PCIE["PCIe root ports 0 / 1"]
    USB["USB-C DRD + ATC PHY"]
  end

  NAND[("NAND")]
  OUT["Outer OLED 5.4in<br/>1398×2034"]
  INN["Inner folding OLED 7.6in<br/>1878 px wide, crease at row 1335"]:::duo
  T1["Touch controller 1<br/>multi-touch"]
  T2["Touch controller 2<br/>multi-touch2"]:::duo
  IMU1["IMU half 1<br/>accel, gyro, hgaccel, compass"]
  IMU2["IMU half 2<br/>accel_1, gyro_1, hgaccel_1, compass_1"]:::duo
  HALL["Hall sensor (Crane)"]
  ALS["ALS incl. als2a/als2b (angle-aware)"]:::duo
  CAM["Cameras: WIDE, SWIDE, FCAM, INTCAM"]
  M3["Secure M3<br/>camera buses"]
  C2["C2 modem<br/>5G, GNSS, satellite"]
  N1["N1<br/>Wi-Fi 7, BT 6, Thread"]
  ROSE["Rose UWB"]
  NFC1["NFC primary + SE<br/>stockholm"]
  NFC2["NFC secondary<br/>hammerfest"]
  PMU1["PMU main (Becketts)"]
  PMU2["PMU secondary (Fairmont)"]:::duo
  BAT["Batteries: 2 packs<br/>BMU + BMU2 gauges"]
  MESA["Touch ID sensor<br/>/arm-io/spi1/mesa"]:::duo
  CODEC["Audio: CS42L79 codec,<br/>CS35L28 amps"]
  TAP["Taptic engine (LEAP)"]

  ANS --- NAND
  DCP --- OUT
  DCPSEC --- INN
  MTP --- T1
  MTP --- T2
  AOP --- IMU1
  AOP --- IMU2
  AOP --- HALL
  AOP --- ALS
  AOP --- CODEC
  AOP --- TAP
  ISP --- CAM
  M3 --- CAM
  PCIE -- "port 1 (Leda)" --- C2
  PCIE -- "port 0, 3 functions" --- N1
  AOP -- SPMI --- NFC1
  AOP -- SPMI --- NFC2
  AOP --- ROSE
  SMC --- PMU1
  PMU1 -- "sgpio bridge" --- PMU2
  SMC --- BAT
  SEP -- "sbio" --- MESA
  AOP2 -. "push keep-alive" .- N1

  classDef duo stroke-dasharray: 5 5
```

## Where the evidence is

| Part of the picture | Chapter | Generated reference |
|---|---|---|
| CPU, AIC, PMGR, memory, ANS, buses | [01](01-soc-cpu-memory-storage.md) | [physical address map](../reference/maps/physical-address-map.md), [interrupt map](../reference/maps/interrupt-map.md), [bus devices](../reference/maps/bus-devices.md) |
| SEP, SPTM, TXM, exclaves, Touch ID | [02](02-boot-and-security.md) | [manifest](../reference/manifest.md) |
| GPU, DCP/DCPSEC/DCPEXT, panels | [03](03-gpu-and-displays.md), [10](10-userland-display-fold-touch.md) | [co-processor matrix](../reference/maps/coprocessors.md) |
| ISP, cameras, Secure M3, AVE/AVD, ANE | [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) | [firmware SBOM](../reference/maps/firmware-sbom.md) |
| AOP/AOP2, IMUs, Hall, ALS, MTP touch, audio, Taptic | [05](05-sensors-touch-audio-haptics.md), [08](08-foldable-system-and-chassis.md) | [function codes](../reference/maps/function-codes.md) |
| SMC, PMUs, batteries, charging | [06](06-power-battery-thermal.md) | [syscfg keys](../reference/maps/syscfg-keys.md), [GPIO pins](../reference/maps/gpio-pins.md) |
| C2, N1, Rose, NFC, USB-C | [07](07-networking-and-connectivity.md), [11](11-userland-radios-power-sensors.md) | [driver matches](../reference/maps/driver-matches.md) |

The diagram simplifies: it omits DARTs (IOMMUs), mailboxes, exclave proxies and per-block power domains, all of which are in the maps. Links drawn between a co-processor and a part mean "the chapters show this co-processor or bus owns that part", not a physical trace; board routing is not in the evidence.
