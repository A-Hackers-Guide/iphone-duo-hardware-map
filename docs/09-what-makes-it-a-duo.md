# 09: What makes it a Duo — the device tree against an iPhone 18 Pro and the VM

The cleanest way to see what hardware is specific to the Duo is to diff its device tree against a sibling built on the same SoC. This chapter compares:

- **Duo:** `DeviceTree.v68ap.im4p`, iPhone19,4, `EmbeddedDeviceTrees-12661.52.3` (iOS 27.2).
- **iPhone 18 Pro:** `DeviceTree.v63ap.im4p`, iPhone19,2, `EmbeddedDeviceTrees-12661.2.20`. This is an **earlier** release of the same device-tree project, so a few differences may come from the version gap rather than the hardware. Where that could matter, it is said.
- **vphone600:** `DeviceTree.vphone600ap.im4p`, iPhone99,11, the virtual iPhone that Apple's virtualization framework presents. This is the hardware the [vphone-duo](https://github.com/A-Hackers-Guide/vphone-duo) emulator runs iOS on.

Full generated diffs: [Duo vs iPhone19,2](../reference/compare/duo-vs-iphone19-2.md) and [Duo vs vphone600](../reference/compare/duo-vs-vphone600.md). Generator: `tools/dt_diff.py`. Everything here is **[DT]** unless marked.

## Nodes only the Duo has (51)

| Group | Nodes | What it means |
|---|---|---|
| Second display pipeline | `/arm-io/dcpsec` (+ `iop-dcpsec-nub`, `-expert`, `-sac-controller`, `-exclave-mailbox`, `-exclave-ioreporting`), `/arm-io/dispsec` (+ `hilo`), `/arm-io/dart-dcpsec`, `/arm-io/dart-dispsec`, `/arm-io/dart-dispsecgrt` and their 7 mappers, `/arm-io/exdisplaypipe1` (+ `-s-proxy`) | A complete second display controller with its own firmware co-processor, IOMMUs and exclave-owned secure pipe, for the inner panel. See [03](03-gpu-and-displays.md). |
| Second panel's identity | `/arm-io/i2c3/display-eeprom-2`, `-2-hi`, `display-eeprom-hi` (+ data children), `/arm-io/i2c3/mogul-display2` | EEPROMs and an authentication chip (`mogul,a1222`) for the second panel, on the same I²C bus as the first. |
| A whole extra I²C bus | `/arm-io/i2c4` (`iic,soft`) with `/arm-io/i2c4/mogul-mlb` | On the 18 Pro, `mogul-mlb` sits on `i2c3`; on the Duo it moved to a new `i2c4`. That frees `i2c3` for the two panels **[INF]**. |
| Second touch controller | `/arm-io/mtp/iop-mtp-nub/multi-touch2`, `sync-agent`, `/arm-io/mt-bt-timestamp-sync` | One touch co-processor driving two sensors, with a sync agent and timestamp sync. See [05](05-sensors-touch-audio-haptics.md). |
| Motion sensors in the other half | `/arm-io/aop/iop-aop-nub/accel_1`, `gyro_1`, `hgaccel_1` | The second IMU, from which the AOP derives the hinge angle. See [08](08-foldable-system-and-chassis.md). |
| Fold-aware light sensing | `als2a`, `als2b` | Two angle-dependent ambient light sensors. |
| Second PMU | `/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary` (`pmu,fairmont`) | A secondary PMU reached through a serial-GPIO bridge on the main PMU. See [06](06-power-battery-thermal.md). |
| Touch ID | `/arm-io/spi1`, `/arm-io/spi1/mesa` (`biosensor,mesa`) | The fingerprint sensor in the side button, on its own SPI controller. The 18 Pro has no SPI1 at all. See [02](02-boot-and-security.md). |
| Repair | `/arm-io/secure-repair` (`secure-repair,1`) | A secure-repair block. **[INF]** It may support pairing replacement parts across the two halves; the version gap means it could also be new in the later device-tree release. |
| Brightness per panel | `/core-brightness/brightness-primary`, `brightness-secondary`, `brightness-secondary-doe1`, `/exbright/contrast-indicator-0/1`, `/display-health-monitor` | Separate brightness tables per panel, and a second inner-panel tuning. |
| Panels as products | `/product/display0`, `/product/display1` | Per-panel geometry: index, rotation (inner = 270°), scale, cut-outs, framebuffer IDs, the fold line. |

## Nodes only the iPhone 18 Pro has (5)

| Node | Meaning on the Duo |
|---|---|
| `/arm-io/pearl-sep` | The Face ID (Pearl) link to the Secure Enclave. Its absence is direct evidence that **the Duo has no Face ID path**, whatever Pearl code remains elsewhere ([12](12-userland-camera-ane-audio-security.md)). |
| `/arm-io/apr`, `/arm-io/dart-apr` (+ mapper) | An `apr,p0` block with its own IOMMU. **[KC]** The kernel's `AppleProResHW` personality matches `apr,p0`, so this is the ProRes engine the Duo lacks. *(Earlier text, kept for context:)* On other recent iPhones `apr` has been associated with ProRes/"Apple ProRes" hardware. That would fit the Duo's missing ProRes hardware path ([12](12-userland-camera-ane-audio-security.md)), but the device tree does not say what `apr` is. |
| `/arm-io/i2c3/mogul-mlb` | Moved to `i2c4` on the Duo (above). |

## `/product`: the same SoC, a different phone

| Property | Duo | iPhone 18 Pro | Reading |
|---|---|---|---|
| `product-name` | iPhone Duo | iPhone 18 Pro | |
| `unique-model` | V68AP | V63AP | |
| `compatible-device-fallback` | iPhone18,3 | iPhone18,1 | What apps without Duo support are treated as. |
| `large-format-phone` | 1 | 0 | |
| `supports-apple-pencil` | 1 | — | Matches the public USB-C Pencil support. |
| `bmu-num-enabled` / `bmu-num-supported` | 2 / **3** | 1 / 1 | Two battery gauges in use. The design allows a third **[INF: a platform maximum rather than a hidden cell]**. |
| `bmu-board-id` / `bmu2-board-id`, `bmu2-chip-id` | 0x8193 / 0x8193, 0xe505 | 0x8191 / 0, 0 | The second gauge exists only on the Duo. |
| `has-prox` | — (inner display node: 0) | 1 | The Duo's product node does not claim a proximity sensor in the same place. See [05](05-sensors-touch-audio-haptics.md). |
| `has-virtualization` | — | 1 | The 18 Pro's tree advertises virtualization support; the Duo's does not. This could be the version gap. |
| `ringer-button-location` | — | present | **The Duo has no ringer/Action button.** Its buttons are side (Touch ID), Camera Control and volume. |
| `special-region-*` | — at `/product` (moved to `/product/display0/1`) | Jindo + NonblankableRR | The Dynamic Island / cut-out description moved into the per-panel nodes. |
| `ui-reachability` | — | 1 | Reachability is not offered on the Duo. |
| `front-cam-rotation-isp` | 0xb4 (180°) | 0x10e (270°) | The front camera is mounted at a different angle. |
| `chrome-identifier` | `…chrome.phone15` | `…chrome.phone11` | Simulator device frame. |

## The virtual iPhone (vphone600) against the Duo

The emulator runs the Duo's iOS on Apple's virtual iPhone hardware, so this diff is the list of what it has to fake or cannot provide.

- **451 of the Duo's 552 nodes are absent from vphone600.** The virtual platform has 143 nodes in all. It has no AOP, AOP2, DCP, ISP, ANE, AVE/AVD, AGX GPU, PMU, SMC or SPMI bus, no touch co-processor, and none of the I²C/SPI devices. It does have a SEP node (`/arm-io/sep` with an `xART` child), i.e. a virtual Secure Enclave. Its compatible string is `AppleVirtualPlatformARM`.
- **One display.** There is no second display pipeline. This is the one-display limit that [08 § What emulation taught us](08-foldable-system-and-chassis.md) describes; the inner panel can only be shown by repointing the single framebuffer.
- **No sensors.** Hinge angle, motion and light all have to be injected in software. The vphone-duo project does this with a virtual HID service in `backboardd`.

See [the full VM diff](../reference/compare/duo-vs-vphone600.md) for the 42 nodes only the VM has (virtio and paravirtual devices) and the 22 shared nodes that differ.

## Limits

- The 18 Pro tree is from an earlier device-tree release (12661.2.20 against 12661.52.3). A node that is "Duo-only" could in principle have been added to every product later. For the display, touch, IMU, PMU and Touch ID groups the hardware meaning makes that unlikely; for `secure-repair` and `has-virtualization` it is a real possibility.
- Node names are compared by path. A node that was renamed shows up on both sides.
