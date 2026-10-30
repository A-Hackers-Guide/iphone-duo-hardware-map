# A tour: how to answer questions with this repo

The repo is large. These worked examples show the path through it for common kinds of question. Each step names the page to open.

## "What hardware does the Duo have that other iPhones don't?"

1. [09: What makes it a Duo](09-what-makes-it-a-duo.md): the 51 device-tree nodes only the Duo has, from a diff against an iPhone 18 Pro.
2. The full diff: [`reference/compare/duo-vs-iphone19-2.md`](../reference/compare/duo-vs-iphone19-2.md).
3. For any node in it, its page under [`reference/devicetree/`](../reference/devicetree/README.md) shows its driver, wiring and every property.

## "How does the phone know it is folded, and who reacts?"

1. [08: The foldable system](08-foldable-system-and-chassis.md) for the whole chain, then [05](05-sensors-touch-audio-haptics.md) for the sensors.
2. Hardware: the two IMUs `accel` / `accel_1` and the Hall sensor (`crane_hes`), all on the AOP. Find them in [`reference/devicetree/`](../reference/devicetree/README.md) under `/arm-io/aop/iop-aop-nub/`.
3. Firmware: the AOP image's angle estimator strings in [`reference/firmware/`](../reference/firmware/README.md) (`aopfw-v68aop`).
4. Kernel: the "Hinge Angle" HID personality in [`com.apple.iokit.IOHIDFamily`](../reference/kexts/com.apple.iokit.IOHIDFamily.md).
5. Userland: [10](10-userland-display-fold-touch.md) for CoreMotion `CMAngleManager`, SpringBoard's pose provider, and the public `UIHinge` API. Class pages under [`reference/objc/`](../reference/objc/README.md).
6. Everyone else who reacts to the angle: display colour ([03](03-gpu-and-displays.md)), auto-brightness ([10](10-userland-display-fold-touch.md)), cellular antennas and SAR ([11](11-userland-radios-power-sensors.md)), the inner camera ([12](12-userland-camera-ane-audio-security.md)).

## "Which driver runs this block, and what does it say in its logs?"

```bash
python3 tools/duomap.py who gpu,t8160
```

Then open the kext page, e.g. [`com.apple.AGXG19P`](../reference/kexts/com.apple.AGXG19P.md), for its personalities, C++ classes and every log string. Each class has its own page under [`reference/kclasses/`](../reference/kclasses/README.md) with its superclass chain.

## "What owns this physical address / interrupt / GPIO pin?"

```bash
python3 tools/duomap.py addr 0x381600000   # the ISP co-processor (/arm-io/ispRtb)
```

```bash
python3 tools/duomap.py irq 1226
```

Or browse [the physical address map](../reference/maps/physical-address-map.md), [the interrupt map](../reference/maps/interrupt-map.md) and [the GPIO pin map](../reference/maps/gpio-pins.md).

## "What firmware runs on each co-processor, and how is it signed?"

1. [The co-processor matrix](../reference/maps/coprocessors.md): node, role, firmware image, OS version, manifest component, drivers.
2. [The BuildManifest page](../reference/manifest.md): every signed component and its trust flags.
3. [13: Lifecycle](13-lifecycle.md): which updater flashes which chip, and which images are only loaded into RAM at boot.

## "Is there a public API for this hardware?"

Start at [MAP](MAP.md): its **Public API** column, with links to the chapter that establishes it. For the full class surface of a framework, open its page under [`reference/userland/`](../reference/userland/README.md) (classes, methods, strings) and its symbol table under [`reference/userland-symbols/`](../reference/userland-symbols/README.md).

## "How sure is this claim?"

Every claim carries an evidence label (see the [README](../README.md#evidence-labels)). Four adversarial fact-check passes re-derived 150 claims from raw evidence and corrected 35: [1](FACTCHECK.md), [2](FACTCHECK-2.md), [3](FACTCHECK-3.md), [4](FACTCHECK-4.md). What remains unknown is listed in [Open questions](OPEN-QUESTIONS.md).
