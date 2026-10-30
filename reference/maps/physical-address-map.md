# Physical address map

Every register window that translates to a CPU physical address through the `ranges` of each parent bus, sorted by address. This is the SoC's memory map as the kernel sees it. **[DT]**

481 windows.

| Start | End | Size | Node | # | Driver |
|---|---|---|---|---|---|
| `0x000000000` | `0x000003fff` | `0x4000` | [`/dart-tlbi-aperture`](../devicetree/root__dart-tlbi-aperture.md) | 0 |  |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 7 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 8 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 9 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 10 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 11 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 12 | AppleASCWrapV8 |
| `0x200000000` | `0x200000000` | `0x0` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 13 | AppleASCWrapV8 |
| `0x210050000` | `0x210051fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 2 | AppleSoCIOPSD |
| `0x210050000` | `0x21005900f` | `0x9010` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 10 | AppleT8160PMGR |
| `0x2100f0000` | `0x2100fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 0 | AppleProcessorTraceT8160 |
| `0x210150000` | `0x210151fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 3 | AppleSoCIOPSD |
| `0x210150000` | `0x21015900f` | `0x9010` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 11 | AppleT8160PMGR |
| `0x2101f0000` | `0x2101fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 1 | AppleProcessorTraceT8160 |
| `0x210250000` | `0x210251fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 4 | AppleSoCIOPSD |
| `0x210250000` | `0x21025900f` | `0x9010` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 12 | AppleT8160PMGR |
| `0x2102f0000` | `0x2102fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 2 | AppleProcessorTraceT8160 |
| `0x210350000` | `0x210351fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 5 | AppleSoCIOPSD |
| `0x210350000` | `0x21035900f` | `0x9010` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 13 | AppleT8160PMGR |
| `0x2103f0000` | `0x2103fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 3 | AppleProcessorTraceT8160 |
| `0x210d00000` | `0x210d0df53` | `0xdf54` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 50 | AppleT8160PMGR |
| `0x210d20000` | `0x210d2dd53` | `0xdd54` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 51 | AppleT8160PMGR |
| `0x210e20000` | `0x210e21267` | `0x1268` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 5 | AppleT8160PMGR |
| `0x210e40000` | `0x210e4c027` | `0xc028` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 7 | AppleT8160PMGR |
| `0x210e40000` | `0x210e4ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) ⚠ overlaps previous | 8 | AppleProcessorTraceT8160 |
| `0x210e50000` | `0x210e5904f` | `0x9050` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 8 | AppleT8160PMGR |
| `0x210e50000` | `0x210e5ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) ⚠ overlaps previous | 10 | AppleProcessorTraceT8160 |
| `0x210e70000` | `0x210e7ffe7` | `0xffe8` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 9 | AppleT8160PMGR |
| `0x210e90000` | `0x210e9ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 12 | AppleProcessorTraceT8160 |
| `0x210eb0000` | `0x210ebffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 14 | AppleProcessorTraceT8160 |
| `0x210f00000` | `0x210f01fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 0 | AppleSoCIOPSD |
| `0x210f00000` | `0x210f40087` | `0x40088` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 6 | AppleT8160PMGR |
| `0x210ff0000` | `0x210ffffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 6 | AppleProcessorTraceT8160 |
| `0x211050000` | `0x211051fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 6 | AppleSoCIOPSD |
| `0x211050000` | `0x21105c027` | `0xc028` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 19 | AppleT8160PMGR |
| `0x2110f0000` | `0x2110fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 4 | AppleProcessorTraceT8160 |
| `0x211150000` | `0x211151fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 7 | AppleSoCIOPSD |
| `0x211150000` | `0x21115c027` | `0xc028` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 20 | AppleT8160PMGR |
| `0x2111f0000` | `0x2111fffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 5 | AppleProcessorTraceT8160 |
| `0x211d00000` | `0x211d0e753` | `0xe754` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 52 | AppleT8160PMGR |
| `0x211d20000` | `0x211d2e953` | `0xe954` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 53 | AppleT8160PMGR |
| `0x211e20000` | `0x211e212e7` | `0x12e8` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 14 | AppleT8160PMGR |
| `0x211e40000` | `0x211e4c027` | `0xc028` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 16 | AppleT8160PMGR |
| `0x211e40000` | `0x211e4ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) ⚠ overlaps previous | 9 | AppleProcessorTraceT8160 |
| `0x211e50000` | `0x211e5904f` | `0x9050` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 17 | AppleT8160PMGR |
| `0x211e50000` | `0x211e5ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) ⚠ overlaps previous | 11 | AppleProcessorTraceT8160 |
| `0x211e70000` | `0x211e7ffe7` | `0xffe8` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 18 | AppleT8160PMGR |
| `0x211e90000` | `0x211e9ffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 13 | AppleProcessorTraceT8160 |
| `0x211eb0000` | `0x211ebffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 15 | AppleProcessorTraceT8160 |
| `0x211f00000` | `0x211f01fff` | `0x2000` | [`/arm-io`](../devicetree/root__arm-io.md) | 1 | AppleSoCIOPSD |
| `0x211f00000` | `0x211f40087` | `0x40088` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 15 | AppleT8160PMGR |
| `0x211ff0000` | `0x211ffffff` | `0x10000` | [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | 7 | AppleProcessorTraceT8160 |
| `0x220000000` | `0x2200fffff` | `0x100000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 1 | AppleT8160MemCacheController |
| `0x221000000` | `0x22100ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 8 | AppleT8160MemCacheController |
| `0x221200000` | `0x22120ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 9 | AppleT8160MemCacheController |
| `0x221400000` | `0x22140ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 10 | AppleT8160MemCacheController |
| `0x221600000` | `0x22160ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 11 | AppleT8160MemCacheController |
| `0x221800000` | `0x22180ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 12 | AppleT8160MemCacheController |
| `0x221a00000` | `0x221a0ffff` | `0x10000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 13 | AppleT8160MemCacheController |
| `0x24f010000` | `0x24f017fff` | `0x8000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 2 | AppleT8160MemCacheController |
| `0x250010000` | `0x250017fff` | `0x8000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 3 | AppleT8160MemCacheController |
| `0x251010000` | `0x251017fff` | `0x8000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 4 | AppleT8160MemCacheController |
| `0x252010000` | `0x252017fff` | `0x8000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | 5 | AppleT8160MemCacheController |
| `0x280000000` | `0x28003ffff` | `0x40000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 2 | AppleT8160PMGR |
| `0x280000000` | `0x28003ffff` | `0x40000` | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) ⚠ overlaps previous | 2 | AppleSoCReporter |
| `0x280000000` | `0x28003ffff` | `0x40000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 0 | AppleEventLogHandler |
| `0x28002003c` | `0x28002003f` | `0x4` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 11 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x280020040` | `0x280020043` | `0x4` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 12 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x28002c000` | `0x28002ffff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 41 | AppleT8160PMGR |
| `0x280210000` | `0x28021bfff` | `0xc000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 27 | AppleT8160PMGR |
| `0x280210000` | `0x280213fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 1 | AppleEventLogHandler |
| `0x280210800` | `0x2802147ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 2 | AppleEventLogHandler |
| `0x280212800` | `0x2802167ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 3 | AppleEventLogHandler |
| `0x280212e00` | `0x280216dff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 4 | AppleEventLogHandler |
| `0x280212f00` | `0x280216eff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 5 | AppleEventLogHandler |
| `0x280213000` | `0x280216fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 6 | AppleEventLogHandler |
| `0x280213600` | `0x2802175ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 7 | AppleEventLogHandler |
| `0x280213700` | `0x2802176ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 8 | AppleEventLogHandler |
| `0x280213800` | `0x2802177ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 9 | AppleEventLogHandler |
| `0x280213e00` | `0x280217dff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 10 | AppleEventLogHandler |
| `0x280213f00` | `0x280217eff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 11 | AppleEventLogHandler |
| `0x280214000` | `0x280217fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 12 | AppleEventLogHandler |
| `0x280214600` | `0x2802185ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 13 | AppleEventLogHandler |
| `0x280214700` | `0x2802186ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 14 | AppleEventLogHandler |
| `0x280214800` | `0x2802187ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 15 | AppleEventLogHandler |
| `0x280214e00` | `0x280218dff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 16 | AppleEventLogHandler |
| `0x280214f00` | `0x280218eff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 17 | AppleEventLogHandler |
| `0x280215000` | `0x280218fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 18 | AppleEventLogHandler |
| `0x280215600` | `0x2802195ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 19 | AppleEventLogHandler |
| `0x280215700` | `0x2802196ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 20 | AppleEventLogHandler |
| `0x280215800` | `0x2802197ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 21 | AppleEventLogHandler |
| `0x280215e00` | `0x280219dff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 22 | AppleEventLogHandler |
| `0x280215f00` | `0x280219eff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 23 | AppleEventLogHandler |
| `0x280216000` | `0x280219fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 24 | AppleEventLogHandler |
| `0x280216600` | `0x28021a5ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 25 | AppleEventLogHandler |
| `0x280216700` | `0x28021a6ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 26 | AppleEventLogHandler |
| `0x280216800` | `0x28021a7ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 27 | AppleEventLogHandler |
| `0x280216e00` | `0x28021adff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 28 | AppleEventLogHandler |
| `0x280216f00` | `0x28021aeff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 29 | AppleEventLogHandler |
| `0x280217000` | `0x28021afff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 30 | AppleEventLogHandler |
| `0x280217600` | `0x28021b5ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 31 | AppleEventLogHandler |
| `0x280217700` | `0x28021b6ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 32 | AppleEventLogHandler |
| `0x280217800` | `0x28021b7ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 33 | AppleEventLogHandler |
| `0x280217a00` | `0x28021b9ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 34 | AppleEventLogHandler |
| `0x280217c00` | `0x28021bbff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 35 | AppleEventLogHandler |
| `0x280217e00` | `0x28021bdff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 36 | AppleEventLogHandler |
| `0x280218000` | `0x28021bfff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 37 | AppleEventLogHandler |
| `0x280218200` | `0x28021c1ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 38 | AppleEventLogHandler |
| `0x280218400` | `0x28021c3ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 39 | AppleEventLogHandler |
| `0x280218600` | `0x28021c5ff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 40 | AppleEventLogHandler |
| `0x280270000` | `0x280273fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 41 | AppleEventLogHandler |
| `0x280274000` | `0x280277fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 42 | AppleEventLogHandler |
| `0x280280000` | `0x280297fff` | `0x18000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 21 | AppleT8160PMGR |
| `0x280280000` | `0x280297fff` | `0x18000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 53 | AppleEventLogHandler |
| `0x2802b0000` | `0x2802b3fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 54 | AppleEventLogHandler |
| `0x2803c0000` | `0x2803dffff` | `0x20000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 37 | AppleT8160PMGR |
| `0x2803c0000` | `0x2803c3fff` | `0x4000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) ⚠ overlaps previous | 6 | AppleT8160MemCacheController |
| `0x2803d0000` | `0x2803d3fff` | `0x4000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) ⚠ overlaps previous | 7 | AppleT8160MemCacheController |
| `0x2803d0000` | `0x2803d3fff` | `0x4000` | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) ⚠ overlaps previous | 4 | AppleASCWrapV8 |
| `0x2803dc000` | `0x2803dffff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 43 | AppleEventLogHandler |
| `0x280400000` | `0x28041bfff` | `0x1c000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 44 | AppleEventLogHandler |
| `0x280440000` | `0x280443fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 45 | AppleEventLogHandler |
| `0x280444000` | `0x280447fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 46 | AppleEventLogHandler |
| `0x280500000` | `0x2805affff` | `0xb0000` | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) | 3 | AppleASCWrapV8 |
| `0x280700000` | `0x2807cffff` | `0xd0000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 0 | AppleT8160PMGR |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 28 | AppleT8160PMGR |
| `0x280700000` | `0x2807cffff` | `0xd0000` | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) ⚠ overlaps previous | 0 | AppleSoCReporter |
| `0x280700000` | `0x2807cffff` | `0xd0000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 47 | AppleEventLogHandler |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) ⚠ overlaps previous | 8 | AppleM2ScalerCSCDriver |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 5 | AppleASCWrapV8SISP |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) ⚠ overlaps previous | 1 | AppleCamera |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) ⚠ overlaps previous | 4 | AppleASCWrapV8ANE |
| `0x280700000` | `0x28071bfff` | `0x1c000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) ⚠ overlaps previous | 4 | AppleASCWrapV8ANE |
| `0x280708000` | `0x28070bfff` | `0x4000` | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) ⚠ overlaps previous | 3 | AppleAVE2Driver |
| `0x280724000` | `0x280727fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 30 | AppleT8160PMGR |
| `0x280724000` | `0x280727fff` | `0x4000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 6 | AppleASCWrapV8SISP |
| `0x280724000` | `0x280727fff` | `0x4000` | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) ⚠ overlaps previous | 2 | AppleCamera |
| `0x280724000` | `0x280727fff` | `0x4000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) ⚠ overlaps previous | 5 | AppleASCWrapV8ANE |
| `0x280724000` | `0x280727fff` | `0x4000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) ⚠ overlaps previous | 5 | AppleASCWrapV8ANE |
| `0x280728000` | `0x28072bfff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 29 | AppleT8160PMGR |
| `0x280730000` | `0x280743fff` | `0x14000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 38 | AppleT8160PMGR |
| `0x280760000` | `0x280763fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 33 | AppleT8160PMGR |
| `0x280764000` | `0x280767fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 31 | AppleT8160PMGR |
| `0x280768000` | `0x28076bfff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 40 | AppleT8160PMGR |
| `0x280780000` | `0x280783fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 32 | AppleT8160PMGR |
| `0x280780000` | `0x280783fff` | `0x4000` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) ⚠ overlaps previous | 0 | AppleT8160MemCacheController |
| `0x280850000` | `0x280853fff` | `0x4000` | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) | 1 | AppleASCWrapV8 |
| `0x280e00000` | `0x280e73fff` | `0x74000` | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) | 0 | AppleASCWrapV8 |
| `0x281000000` | `0x2811cbfff` | `0x1cc000` | [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) | 0 | AppleInterruptControllerV3 |
| `0x282800000` | `0x2829d3fff` | `0x1d4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 42 | AppleT8160PMGR |
| `0x282800000` | `0x2829d3fff` | `0x1d4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 48 | AppleEventLogHandler |
| `0x282800000` | `0x2829d3fff` | `0x1d4000` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) ⚠ overlaps previous | 4 | AppleCLCD2 |
| `0x282800000` | `0x2829d3fff` | `0x1d4000` | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) ⚠ overlaps previous | 4 | AppleCLCD2 |
| `0x282800000` | `0x2829d3fff` | `0x1d4000` | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) ⚠ overlaps previous | 4 | AppleCLCD2 |
| `0x282838000` | `0x282838007` | `0x8` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 9 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x283000000` | `0x283ffffff` | `0x1000000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 48 | AppleT8160PMGR |
| `0x283000000` | `0x283ffffff` | `0x1000000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 49 | AppleEventLogHandler |
| `0x288000000` | `0x288000fff` | `0x1000` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) | 3 | AppleSoCMisc |
| `0x288004000` | `0x288004fff` | `0x1000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 4 | AppleT8160PMGR |
| `0x288004000` | `0x28800407f` | `0x80` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) ⚠ overlaps previous | 0 | AppleSoCMisc |
| `0x288078000` | `0x28807bfff` | `0x4000` | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) | 2 | AppleS8000AESAccelerator |
| `0x288078000` | `0x28807bfff` | `0x4000` | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) ⚠ overlaps previous | 1 | AppleAVD |
| `0x288080000` | `0x288083fff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 50 | AppleEventLogHandler |
| `0x288100000` | `0x2881a7fff` | `0xa8000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 23 | AppleT8160PMGR |
| `0x28810c000` | `0x28810cfff` | `0x1000` | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) ⚠ overlaps previous | 1 | AppleSerialShim |
| `0x288128000` | `0x288137fff` | `0x10000` | [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) ⚠ overlaps previous | 0 | AppleSerialShim |
| `0x2881f0000` | `0x2881f3fff` | `0x4000` | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | 0 | AppleT8101GPIOIC |
| `0x288200000` | `0x28823ffff` | `0x40000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 3 | AppleT8160PMGR |
| `0x288200000` | `0x28823ffff` | `0x40000` | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) ⚠ overlaps previous | 3 | AppleSoCReporter |
| `0x288200000` | `0x28823ffff` | `0x40000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 51 | AppleEventLogHandler |
| `0x288280000` | `0x2882fffff` | `0x80000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 1 | AppleT8160PMGR |
| `0x288280000` | `0x2882fffff` | `0x80000` | [`/arm-io/soc-reporter`](../devicetree/root__arm-io__soc-reporter.md) ⚠ overlaps previous | 1 | AppleSoCReporter |
| `0x288280000` | `0x2882fffff` | `0x80000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 52 | AppleEventLogHandler |
| `0x2882a8000` | `0x2882abfff` | `0x4000` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) ⚠ overlaps previous | 5 | AppleSoCMisc |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) ⚠ overlaps previous | 5 | AppleASCWrapV8 |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882a8000` | `0x2882a8007` | `0x8` | [`/arm-io/admac-leap-s`](../devicetree/root__arm-io__admac-leap-s.md) ⚠ overlaps previous | 1 | AudioDMAController |
| `0x2882b0000` | `0x2882b3fff` | `0x4000` | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) ⚠ overlaps previous | 0 | AppleARMWatchdogTimer |
| `0x2882b8000` | `0x2882c7fff` | `0x10000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 34 | AppleT8160PMGR |
| `0x2882b8000` | `0x2882c7fff` | `0x10000` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) ⚠ overlaps previous | 4 | AppleSoCMisc |
| `0x2882b8008` | `0x2882b800b` | `0x4` | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) ⚠ overlaps previous | 2 | AppleARMWatchdogTimer |
| `0x2882b8020` | `0x2882b8023` | `0x4` | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) ⚠ overlaps previous | 4 | AppleARMWatchdogTimer |
| `0x2882b802c` | `0x2882b802f` | `0x4` | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) ⚠ overlaps previous | 3 | AppleARMWatchdogTimer |
| `0x2882bc058` | `0x2882bc05b` | `0x4` | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) ⚠ overlaps previous | 1 | AppleARMWatchdogTimer |
| `0x2882c8000` | `0x2882cbfff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 35 | AppleT8160PMGR |
| `0x2882d0000` | `0x2882d3fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 36 | AppleT8160PMGR |
| `0x2882d0000` | `0x2882d0bff` | `0xc00` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) ⚠ overlaps previous | 2 | AppleSoCMisc |
| `0x2882dc000` | `0x2882dc127` | `0x128` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) ⚠ overlaps previous | 1 | AppleSoCMisc |
| `0x2882dc000` | `0x2882e3fff` | `0x8000` | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) ⚠ overlaps previous | 1 | AppleS8000AESAccelerator |
| `0x2885c0000` | `0x2885d7fff` | `0x18000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | 55 | AppleEventLogHandler |
| `0x288600000` | `0x288603fff` | `0x4000` | [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) | 2 | AppleSPMIController |
| `0x288604000` | `0x288607fff` | `0x4000` | [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) | 1 | AppleSPMIController |
| `0x288614000` | `0x288617fff` | `0x4000` | [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) | 0 | AppleSPMIController |
| `0x288700000` | `0x288703fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 22 | AppleT8160PMGR |
| `0x288700000` | `0x288703fff` | `0x4000` | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) ⚠ overlaps previous | 2 | AppleSPMIController |
| `0x288704000` | `0x288707fff` | `0x4000` | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) | 1 | AppleSPMIController |
| `0x288714000` | `0x288717fff` | `0x4000` | [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) | 0 | AppleSPMIController |
| `0x288900000` | `0x288903fff` | `0x4000` | [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) | 2 | AppleSPMIController |
| `0x288904000` | `0x288907fff` | `0x4000` | [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) | 1 | AppleSPMIController |
| `0x288914000` | `0x288917fff` | `0x4000` | [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) | 0 | AppleSPMIController |
| `0x289825000` | `0x289828fff` | `0x4000` | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) | 0 |  |
| `0x2898c0000` | `0x2898c0003` | `0x4` | [`/arm-io/rsm`](../devicetree/root__arm-io__rsm.md) | 1 |  |
| `0x2899c0000` | `0x2899c3fff` | `0x4000` | [`/arm-io/dbgCPU`](../devicetree/root__arm-io__dbgCPU.md) | 1 |  |
| `0x289b00000` | `0x289b1ffff` | `0x20000` | [`/arm-io/dbgCPU`](../devicetree/root__arm-io__dbgCPU.md) | 0 |  |
| `0x289b78000` | `0x289b87fff` | `0x10000` | [`/arm-io/dbgCPU`](../devicetree/root__arm-io__dbgCPU.md) | 2 |  |
| `0x28c050000` | `0x28c053fff` | `0x4000` | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) | 1 | AppleASCWrapV8 |
| `0x28c600000` | `0x28c673fff` | `0x74000` | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) | 0 | AppleASCWrapV8 |
| `0x28c810000` | `0x28c8100ff` | `0x100` | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) | 3 | AppleASCWrapV8 |
| `0x28c820000` | `0x28c823fff` | `0x4000` | [`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) | 0 | AppleT8101GPIOIC |
| `0x28c840000` | `0x28c843fff` | `0x4000` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | 0 | ApplePTD, AppleSPUAONPTDDriver |
| `0x28c850000` | `0x28c853fff` | `0x4000` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | 1 | ApplePTD, AppleSPUAONPTDDriver |
| `0x28c858000` | `0x28c85bfff` | `0x4000` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | 2 | ApplePTD, AppleSPUAONPTDDriver |
| `0x28c860000` | `0x28c863fff` | `0x4000` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | 3 | ApplePTD, AppleSPUAONPTDDriver |
| `0x290050000` | `0x290053fff` | `0x4000` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) | 1 | AppleASCWrapV8 |
| `0x290600000` | `0x290673fff` | `0x74000` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) | 0 | AppleASCWrapV8 |
| `0x29060c000` | `0x290648007` | `0x3c008` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) ⚠ overlaps previous | 4 | AppleASCWrapV8 |
| `0x290824000` | `0x290827fff` | `0x4000` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | 0 | AppleT8101GPIOIC |
| `0x290824000` | `0x290827fff` | `0x4000` | [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) ⚠ overlaps previous | 0 | AppleSecureRepair |
| `0x290900000` | `0x290903fff` | `0x4000` | [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) | 2 | AppleSPMIController |
| `0x290904000` | `0x290907fff` | `0x4000` | [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) | 1 | AppleSPMIController |
| `0x290914000` | `0x290917fff` | `0x4000` | [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) | 0 | AppleSPMIController |
| `0x290b00000` | `0x290b03fff` | `0x4000` | [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) | 2 | AppleSPMIController |
| `0x290b04000` | `0x290b07fff` | `0x4000` | [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) | 1 | AppleSPMIController |
| `0x290b14000` | `0x290b17fff` | `0x4000` | [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) | 0 | AppleSPMIController |
| `0x290c00000` | `0x290ddffff` | `0x1e0000` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) | 3 | AppleASCWrapV8 |
| `0x291050000` | `0x291053fff` | `0x4000` | [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) | 1 | AppleASCWrapV8 |
| `0x291600000` | `0x291673fff` | `0x74000` | [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) | 0 | AppleASCWrapV8 |
| `0x29160c000` | `0x291648007` | `0x3c008` | [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) ⚠ overlaps previous | 3 | AppleASCWrapV8 |
| `0x293100000` | `0x2931a3fff` | `0xa4000` | [`/arm-io/admac-leap-s`](../devicetree/root__arm-io__admac-leap-s.md) | 0 | AudioDMAController |
| `0x293300000` | `0x2933a3fff` | `0xa4000` | [`/arm-io/admac-leap-ns`](../devicetree/root__arm-io__admac-leap-ns.md) | 0 | AudioDMAController |
| `0x293700000` | `0x2937b7fff` | `0xb8000` | [`/arm-io/admac-base-s`](../devicetree/root__arm-io__admac-base-s.md) | 0 | AudioDMAController |
| `0x293900000` | `0x2939b3fff` | `0xb4000` | [`/arm-io/admac-base-ns`](../devicetree/root__arm-io__admac-base-ns.md) | 0 | AudioDMAController |
| `0x293c80000` | `0x293c83fff` | `0x4000` | [`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) | 0 | AudioDMACLLTEscalationDetector |
| `0x293c84000` | `0x293c87fff` | `0x4000` | [`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) | 1 | AudioDMACLLTEscalationDetector |
| `0x294050000` | `0x294053fff` | `0x4000` | [`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) | 1 | AppleASCWrapV8 |
| `0x294600000` | `0x294673fff` | `0x74000` | [`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) | 0 | AppleASCWrapV8 |
| `0x29481c000` | `0x29481ffff` | `0x4000` | [`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) | 0 | AppleT8101GPIOIC |
| `0x296000000` | `0x2961fbfff` | `0x1fc000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | 49 | AppleT8160PMGR |
| `0x296000000` | `0x29601bfff` | `0x1c000` | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) ⚠ overlaps previous | 2 | AppleAVD |
| `0x296000000` | `0x29601bfff` | `0x1c000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) ⚠ overlaps previous | 2 | AppleASCWrapV8ANE |
| `0x296000000` | `0x29601bfff` | `0x1c000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) ⚠ overlaps previous | 2 | AppleASCWrapV8ANE |
| `0x296000000` | `0x29601bfff` | `0x1c000` | [`/arm-io/gfx-asc`](../devicetree/root__arm-io__gfx-asc.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296000000` | `0x29601bfff` | `0x1c000` | [`/arm-io/gfx1-asc`](../devicetree/root__arm-io__gfx1-asc.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) ⚠ overlaps previous | 2 | AppleASCWrapV8 |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) ⚠ overlaps previous | 11 | AppleM2ScalerCSCDriver |
| `0x296020000` | `0x29602ffff` | `0x10000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 2 | AppleASCWrapV8SISP |
| `0x298100000` | `0x29810bfff` | `0xc000` | [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) | 0 | AppleT8110DART |
| `0x29a000000` | `0x29a0fffff` | `0x100000` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | 0 | AppleT8101GPIOIC |
| `0x29a100000` | `0x29a103fff` | `0x4000` | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) | 1 | AppleMSGKext |
| `0x29a800000` | `0x29a833fff` | `0x34000` | [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) | 0 | AppleMSGKext |
| `0x2a0c80000` | `0x2a0c9ffff` | `0x20000` | [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) | 0 | AppleT8110DART |
| `0x2a2050000` | `0x2a20affff` | `0x60000` | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) | 1 | AppleASCWrapV8SEP |
| `0x2a2600000` | `0x2a2673fff` | `0x74000` | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) | 0 | AppleASCWrapV8SEP |
| `0x2a2700000` | `0x2a2713fff` | `0x14000` | [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) | 2 | AppleASCWrapV8SEP |
| `0x2a500c000` | `0x2a500ffff` | `0x4000` | [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) | 0 | AppleS8000AESAccelerator |
| `0x2a5018000` | `0x2a501bfff` | `0x4000` | [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) | 0 | AppleARMSoftIICController, AppleS5L8940XI2CController |
| `0x2a501c000` | `0x2a501ffff` | `0x4000` | [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) | 0 | AppleARMSoftIICController, AppleS5L8940XI2CController |
| `0x2a5020000` | `0x2a5023fff` | `0x4000` | [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) | 0 | AppleARMSoftIICController, AppleS5L8940XI2CController |
| `0x2a5040000` | `0x2a5043fff` | `0x4000` | [`/arm-io/fpwm`](../devicetree/root__arm-io__fpwm.md) | 0 | AppleS5L8920XFPWM |
| `0x2a5060000` | `0x2a507ffff` | `0x20000` | [`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) | 0 | AppleT8110DART |
| `0x2a5104000` | `0x2a5107fff` | `0x4000` | [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) | 0 | AppleSPIMCController |
| `0x2a5200000` | `0x2a5203fff` | `0x4000` | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | 0 | AppleSamsungSerial, AppleSerialShim |
| `0x2a5850000` | `0x2a5853fff` | `0x4000` | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) | 1 | AppleASCWrapV8 |
| `0x2a5e00000` | `0x2a5e73fff` | `0x74000` | [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) | 0 | AppleASCWrapV8 |
| `0x2a8000000` | `0x2abffffff` | `0x4000000` | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) | 0 | AGXAcceleratorG19P |
| `0x2a8d00000` | `0x2a8e7ffff` | `0x180000` | [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) ⚠ overlaps previous | 1 | AGXAcceleratorG19P |
| `0x2a8e30000` | `0x2a8e33fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 46 | AppleT8160PMGR |
| `0x2a8e30000` | `0x2a8e37fff` | `0x8000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 47 | AppleT8160PMGR |
| `0x2a8e80000` | `0x2a8eaffff` | `0x30000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 43 | AppleT8160PMGR |
| `0x2a8ec0000` | `0x2a8ec3fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 44 | AppleT8160PMGR |
| `0x2a8ec0000` | `0x2a8ec7fff` | `0x8000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 45 | AppleT8160PMGR |
| `0x2aa050000` | `0x2aa050007` | `0x8` | [`/arm-io/gfx-asc`](../devicetree/root__arm-io__gfx-asc.md) ⚠ overlaps previous | 1 | AppleASCWrapV8 |
| `0x2aa600000` | `0x2aa673fff` | `0x74000` | [`/arm-io/gfx-asc`](../devicetree/root__arm-io__gfx-asc.md) ⚠ overlaps previous | 0 | AppleASCWrapV8 |
| `0x2aa850000` | `0x2aa850007` | `0x8` | [`/arm-io/gfx1-asc`](../devicetree/root__arm-io__gfx1-asc.md) ⚠ overlaps previous | 1 | AppleASCWrapV8 |
| `0x2aae00000` | `0x2aae73fff` | `0x74000` | [`/arm-io/gfx1-asc`](../devicetree/root__arm-io__gfx1-asc.md) ⚠ overlaps previous | 0 | AppleASCWrapV8 |
| `0x301050000` | `0x301053fff` | `0x4000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 1 | AppleASCWrapV8 |
| `0x301600000` | `0x301673fff` | `0x74000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 0 | AppleASCWrapV8 |
| `0x303000000` | `0x303ffffff` | `0x1000000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 4 | AppleASCWrapV8 |
| `0x305040000` | `0x305043fff` | `0x4000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 14 | AppleASCWrapV8 |
| `0x305b90000` | `0x305b9ffff` | `0x10000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 5 | AppleASCWrapV8 |
| `0x305c50000` | `0x305c5bfff` | `0xc000` | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) | 0 | IOCoastGuardSARTMapper |
| `0x305cc0000` | `0x305d1ffff` | `0x60000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | 3 | AppleASCWrapV8 |
| `0x305cc0000` | `0x305cc3fff` | `0x4000` | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) ⚠ overlaps previous | 2 | IOCoastGuardSARTMapper |
| `0x305d44000` | `0x305d47fff` | `0x4000` | [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) | 1 | IOCoastGuardSARTMapper |
| `0x305d47c00` | `0x305d4bbff` | `0x4000` | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) ⚠ overlaps previous | 6 | AppleASCWrapV8 |
| `0x308000000` | `0x30801ffff` | `0x20000` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | 0 | AppleT8110DART |
| `0x308024000` | `0x308033fff` | `0x10000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 9 | AppleT8160PCIe |
| `0x308028000` | `0x30802bfff` | `0x4000` | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) ⚠ overlaps previous | 1 | APCIECoreRCGen5PLCE |
| `0x30802c000` | `0x30802ffff` | `0x4000` | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) ⚠ overlaps previous | 2 | APCIECoreRCGen5PLCE |
| `0x308034000` | `0x308037fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 10 | AppleT8160PCIe |
| `0x30803c000` | `0x30803ffff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 14 | AppleT8160PCIe |
| `0x308040000` | `0x308043fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 13 | AppleT8160PCIe |
| `0x308048000` | `0x30804bfff` | `0x4000` | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) | 0 | ApplePCIePIODMA |
| `0x30804c000` | `0x30804ffff` | `0x4000` | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) | 1 | ApplePCIePIODMA |
| `0x308050000` | `0x308053fff` | `0x4000` | [`/arm-io/apcie0-piodma`](../devicetree/root__arm-io__apcie0-piodma.md) | 2 | ApplePCIePIODMA |
| `0x308054000` | `0x308057fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 12 | AppleT8160PCIe |
| `0x309000000` | `0x30901ffff` | `0x20000` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | 0 | AppleT8110DART |
| `0x309024000` | `0x309033fff` | `0x10000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 15 | AppleT8160PCIe |
| `0x309028000` | `0x30902bfff` | `0x4000` | [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) ⚠ overlaps previous | 1 | APCIECoreRCGen5PLCE |
| `0x30902c000` | `0x30902ffff` | `0x4000` | [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) ⚠ overlaps previous | 2 | APCIECoreRCGen5PLCE |
| `0x309034000` | `0x309037fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 16 | AppleT8160PCIe |
| `0x30903c000` | `0x30903ffff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 20 | AppleT8160PCIe |
| `0x309040000` | `0x309043fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 19 | AppleT8160PCIe |
| `0x309048000` | `0x30904bfff` | `0x4000` | [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) | 0 | ApplePCIePIODMA |
| `0x30904c000` | `0x30904ffff` | `0x4000` | [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) | 1 | ApplePCIePIODMA |
| `0x309050000` | `0x309053fff` | `0x4000` | [`/arm-io/apcie1-piodma`](../devicetree/root__arm-io__apcie1-piodma.md) | 2 | ApplePCIePIODMA |
| `0x309054000` | `0x309057fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 18 | AppleT8160PCIe |
| `0x30c000000` | `0x30c003fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 1 | AppleT8160PCIe |
| `0x30d028000` | `0x30d02bfff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 6 | AppleT8160PCIe |
| `0x30d990000` | `0x30d993fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 8 | AppleT8160PCIe |
| `0x30d990400` | `0x30d9943ff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) ⚠ overlaps previous | 7 | AppleT8160PCIe |
| `0x30e000000` | `0x30effffff` | `0x1000000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 5 | AppleT8160PCIe |
| `0x30f000000` | `0x30f7fffff` | `0x800000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 2 | AppleT8160PCIe |
| `0x30f010000` | `0x30f013fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) ⚠ overlaps previous | 11 | AppleT8160PCIe |
| `0x30f014000` | `0x30f017fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) ⚠ overlaps previous | 17 | AppleT8160PCIe |
| `0x30f020000` | `0x30f023fff` | `0x4000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) ⚠ overlaps previous | 3 | AppleT8160PCIe |
| `0x30f800000` | `0x30f9b7fff` | `0x1b8000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 4 | AppleT8160PCIe |
| `0x320000000` | `0x320ffffff` | `0x1000000` | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) | 3 | AppleT8160TypeCPhy |
| `0x322410000` | `0x322413fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | 5 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322414000` | `0x322417fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | 3 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322418000` | `0x32241bfff` | `0x4000` | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) | 0 | AppleT8160TypeCPhy |
| `0x322430000` | `0x3224417ff` | `0x11800` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | 0 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x32243c000` | `0x3224417ff` | `0x5800` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 2 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x32243d000` | `0x322440fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 7 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322440000` | `0x322443fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 1 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322444000` | `0x322447fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | 6 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322448000` | `0x32244bfff` | `0x4000` | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) | 1 | AppleT8160TypeCPhy |
| `0x322448000` | `0x32244bfff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 4 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x322450000` | `0x322453fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | 8 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x323000000` | `0x323083fff` | `0x84000` | [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) | 2 | AppleT8160TypeCPhy |
| `0x323020000` | `0x32303ffff` | `0x20000` | [`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) ⚠ overlaps previous | 0 | AppleT8110DART |
| `0x323040000` | `0x32305ffff` | `0x20000` | [`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) ⚠ overlaps previous | 1 | AppleT8110DART |
| `0x323074000` | `0x323077fff` | `0x4000` | [`/arm-io/atc0-dpxbar`](../devicetree/root__arm-io__atc0-dpxbar.md) ⚠ overlaps previous | 0 | AppleT602XATCDPXBAR |
| `0x323080000` | `0x323083fff` | `0x4000` | [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) ⚠ overlaps previous | 10 | AppleT8160USBXDCI, AppleT8160USBXHCI |
| `0x380000000` | `0x380007fff` | `0x8000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | 3 | AppleASCWrapV8SISP |
| `0x380000000` | `0x383ffffff` | `0x4000000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 4 | AppleASCWrapV8SISP |
| `0x380000000` | `0x383ffffff` | `0x4000000` | [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) ⚠ overlaps previous | 0 | AppleCamera |
| `0x381050000` | `0x381053fff` | `0x4000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 1 | AppleASCWrapV8SISP |
| `0x381600000` | `0x381673fff` | `0x74000` | [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) ⚠ overlaps previous | 0 | AppleASCWrapV8SISP |
| `0x382b40000` | `0x382b4bfff` | `0xc000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 0 | AppleT8110DART |
| `0x382b50000` | `0x382b53fff` | `0x4000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 5 | AppleT8110DART |
| `0x382b60000` | `0x382b6bfff` | `0xc000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 1 | AppleT8110DART |
| `0x382b74000` | `0x382b77fff` | `0x4000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 3 | AppleT8110DART |
| `0x382b80000` | `0x382b8bfff` | `0xc000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 2 | AppleT8110DART |
| `0x382b94000` | `0x382b97fff` | `0x4000` | [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) ⚠ overlaps previous | 4 | AppleT8110DART |
| `0x384000000` | `0x384e2bfff` | `0xe2c000` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | 0 | AppleCLCD2 |
| `0x386140000` | `0x3861c3fff` | `0x84000` | [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) | 0 | AudioDMAController |
| `0x386240000` | `0x38625ffff` | `0x20000` | [`/arm-io/dart-disp0-isoc`](../devicetree/root__arm-io__dart-disp0-isoc.md) | 0 | AppleT8110DART |
| `0x386260000` | `0x386263fff` | `0x4000` | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) | 1 | AudioDMACLLTEscalationDetector |
| `0x3862c0000` | `0x3862cffff` | `0x10000` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | 1 | AppleCLCD2 |
| `0x386318000` | `0x38631803f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 1 | AppleDCPExpert |
| `0x386368000` | `0x38636803f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 15 | AppleDCPExpert |
| `0x38636c000` | `0x38636ffff` | `0x4000` | [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) | 0 | AudioDMACLLTEscalationDetector |
| `0x386380000` | `0x38638bfff` | `0xc000` | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) | 0 | AppleT8110DART |
| `0x386394000` | `0x386397fff` | `0x4000` | [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) | 1 | AppleT8110DART |
| `0x3863a0000` | `0x3863abfff` | `0xc000` | [`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) | 0 | AppleT8110DART |
| `0x3863b4000` | `0x3863b7fff` | `0x4000` | [`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) | 1 | AppleT8110DART |
| `0x3863c0000` | `0x3863dffff` | `0x20000` | [`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) | 0 | AppleT8110DART |
| `0x3863f4000` | `0x3863f403f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 2 | AppleDCPExpert |
| `0x3863f8000` | `0x3863f803f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 3 | AppleDCPExpert |
| `0x3863fc000` | `0x3863fc03f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 5 | AppleDCPExpert |
| `0x386400000` | `0x38640003f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 6 | AppleDCPExpert |
| `0x386404000` | `0x38640403f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 4 | AppleDCPExpert |
| `0x386408000` | `0x38640803f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 8 | AppleDCPExpert |
| `0x38640c000` | `0x38640c03f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 9 | AppleDCPExpert |
| `0x386410000` | `0x38641003f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 12 | AppleDCPExpert |
| `0x386414000` | `0x38641403f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 10 | AppleDCPExpert |
| `0x386418000` | `0x38641803f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 11 | AppleDCPExpert |
| `0x38641c000` | `0x38641c03f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 13 | AppleDCPExpert |
| `0x386420000` | `0x38642003f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 14 | AppleDCPExpert |
| `0x38642c000` | `0x38642ffff` | `0x4000` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | 2 | AppleCLCD2 |
| `0x38642c0d0` | `0x38642c0d3` | `0x4` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) ⚠ overlaps previous | 0 | AppleDCPExpert |
| `0x386440000` | `0x38644003f` | `0x40` | [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | 7 | AppleDCPExpert |
| `0x386800000` | `0x386ff3fff` | `0x7f4000` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | 3 | AppleCLCD2 |
| `0x386850000` | `0x386853fff` | `0x4000` | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) ⚠ overlaps previous | 1 | AppleASCWrapV8 |
| `0x386e00000` | `0x386e73fff` | `0x74000` | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) ⚠ overlaps previous | 0 | AppleASCWrapV8 |
| `0x386e0c000` | `0x386e48007` | `0x3c008` | [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) ⚠ overlaps previous | 3 | AppleASCWrapV8 |
| `0x388000000` | `0x388e2bfff` | `0xe2c000` | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | 0 | AppleCLCD2 |
| `0x38a2c0000` | `0x38a2cffff` | `0x10000` | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | 1 | AppleCLCD2 |
| `0x38a318000` | `0x38a31803f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 1 | AppleDCPExpert |
| `0x38a368000` | `0x38a36803f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 15 | AppleDCPExpert |
| `0x38a380000` | `0x38a38bfff` | `0xc000` | [`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) | 0 | AppleT8110DART |
| `0x38a394000` | `0x38a397fff` | `0x4000` | [`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) | 1 | AppleT8110DART |
| `0x38a3a0000` | `0x38a3abfff` | `0xc000` | [`/arm-io/dart-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt.md) | 0 | AppleT8110DART |
| `0x38a3b4000` | `0x38a3b7fff` | `0x4000` | [`/arm-io/dart-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt.md) | 1 | AppleT8110DART |
| `0x38a3c0000` | `0x38a3dffff` | `0x20000` | [`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) | 0 | AppleT8110DART |
| `0x38a3f4000` | `0x38a3f403f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 2 | AppleDCPExpert |
| `0x38a3f8000` | `0x38a3f803f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 3 | AppleDCPExpert |
| `0x38a3fc000` | `0x38a3fc03f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 5 | AppleDCPExpert |
| `0x38a400000` | `0x38a40003f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 6 | AppleDCPExpert |
| `0x38a404000` | `0x38a40403f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 4 | AppleDCPExpert |
| `0x38a408000` | `0x38a40803f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 8 | AppleDCPExpert |
| `0x38a40c000` | `0x38a40c03f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 9 | AppleDCPExpert |
| `0x38a410000` | `0x38a41003f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 12 | AppleDCPExpert |
| `0x38a414000` | `0x38a41403f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 10 | AppleDCPExpert |
| `0x38a418000` | `0x38a41803f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 11 | AppleDCPExpert |
| `0x38a41c000` | `0x38a41c03f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 13 | AppleDCPExpert |
| `0x38a420000` | `0x38a42003f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 14 | AppleDCPExpert |
| `0x38a42c000` | `0x38a42ffff` | `0x4000` | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | 2 | AppleCLCD2 |
| `0x38a42c0d0` | `0x38a42c0d3` | `0x4` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) ⚠ overlaps previous | 0 | AppleDCPExpert |
| `0x38a440000` | `0x38a44003f` | `0x40` | [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | 7 | AppleDCPExpert |
| `0x38a800000` | `0x38aff3fff` | `0x7f4000` | [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | 3 | AppleCLCD2 |
| `0x38a850000` | `0x38a853fff` | `0x4000` | [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) ⚠ overlaps previous | 1 | AppleASCWrapV8 |
| `0x38ae00000` | `0x38ae73fff` | `0x74000` | [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) ⚠ overlaps previous | 0 | AppleASCWrapV8 |
| `0x38ae0c000` | `0x38ae48007` | `0x3c008` | [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) ⚠ overlaps previous | 3 | AppleASCWrapV8 |
| `0x38c000000` | `0x38ce2bfff` | `0xe2c000` | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | 0 | AppleCLCD2 |
| `0x38e140000` | `0x38e1c3fff` | `0x84000` | [`/arm-io/admac-dispext0`](../devicetree/root__arm-io__admac-dispext0.md) | 0 | AudioDMAController |
| `0x38e240000` | `0x38e25ffff` | `0x20000` | [`/arm-io/dart-dispext0-isoc`](../devicetree/root__arm-io__dart-dispext0-isoc.md) | 0 | AppleT8110DART |
| `0x38e260000` | `0x38e263fff` | `0x4000` | [`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) | 1 | AudioDMACLLTEscalationDetector |
| `0x38e2c0000` | `0x38e2cffff` | `0x10000` | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | 1 | AppleCLCD2 |
| `0x38e318000` | `0x38e31803f` | `0x40` | [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) | 1 | AppleDCPExpert |
| `0x38e36c000` | `0x38e36ffff` | `0x4000` | [`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) | 0 | AudioDMACLLTEscalationDetector |
| `0x38e380000` | `0x38e38bfff` | `0xc000` | [`/arm-io/dart-dispext0`](../devicetree/root__arm-io__dart-dispext0.md) | 0 | AppleT8110DART |
| `0x38e394000` | `0x38e397fff` | `0x4000` | [`/arm-io/dart-dispext0`](../devicetree/root__arm-io__dart-dispext0.md) | 1 | AppleT8110DART |
| `0x38e3c0000` | `0x38e3cbfff` | `0xc000` | [`/arm-io/dart-dcpext0`](../devicetree/root__arm-io__dart-dcpext0.md) | 0 | AppleT8110DART |
| `0x38e3f4000` | `0x38e3f403f` | `0x40` | [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) | 2 | AppleDCPExpert |
| `0x38e42c000` | `0x38e42ffff` | `0x4000` | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | 2 | AppleCLCD2 |
| `0x38e42c0d0` | `0x38e42c0d3` | `0x4` | [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) ⚠ overlaps previous | 0 | AppleDCPExpert |
| `0x38e800000` | `0x38eff3fff` | `0x7f4000` | [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | 3 | AppleCLCD2 |
| `0x38e850000` | `0x38e853fff` | `0x4000` | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) ⚠ overlaps previous | 1 | AppleASCWrapV8 |
| `0x38ee00000` | `0x38ee73fff` | `0x74000` | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) ⚠ overlaps previous | 0 | AppleASCWrapV8 |
| `0x38ee0c000` | `0x38ee48007` | `0x3c008` | [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) ⚠ overlaps previous | 3 | AppleASCWrapV8 |
| `0x400000000` | `0x400ffffff` | `0x1000000` | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | 4 | AppleAVE2Driver |
| `0x401000000` | `0x4017f3fff` | `0x7f4000` | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | 1 | AppleAVE2Driver |
| `0x403020000` | `0x40303ffff` | `0x20000` | [`/arm-io/dart-ave`](../devicetree/root__arm-io__dart-ave.md) | 0 | AppleT8110DART |
| `0x403030000` | `0x403033fff` | `0x4000` | [`/arm-io/dart-ave`](../devicetree/root__arm-io__dart-ave.md) ⚠ overlaps previous | 1 | AppleT8110DART |
| `0x403050000` | `0x403053fff` | `0x4000` | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | 2 | AppleAVE2Driver |
| `0x403064000` | `0x403067fff` | `0x4000` | [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | 0 | AppleAVE2Driver |
| `0x404000000` | `0x40563bfff` | `0x163c000` | [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) | 0 | AppleAVD |
| `0x405020000` | `0x40503ffff` | `0x20000` | [`/arm-io/dart-avd`](../devicetree/root__arm-io__dart-avd.md) ⚠ overlaps previous | 0 | AppleT8110DART |
| `0x407000000` | `0x407003fff` | `0x4000` | [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) | 0 | AppleJPEGDriver |
| `0x407020000` | `0x40702bfff` | `0xc000` | [`/arm-io/dart-jpeg`](../devicetree/root__arm-io__dart-jpeg.md) | 0 | AppleT8110DART |
| `0x408000000` | `0x408007fff` | `0x8000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 3 | AppleM2ScalerCSCDriver |
| `0x409000000` | `0x409013fff` | `0x14000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 0 | AppleM2ScalerCSCDriver |
| `0x409204000` | `0x409207fff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 2 | AppleM2ScalerCSCDriver |
| `0x409208000` | `0x40920bfff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 7 | AppleM2ScalerCSCDriver |
| `0x409210000` | `0x409213fff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 1 | AppleM2ScalerCSCDriver |
| `0x409210000` | `0x409213fff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) ⚠ overlaps previous | 9 | AppleM2ScalerCSCDriver |
| `0x409220000` | `0x409223fff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 10 | AppleM2ScalerCSCDriver |
| `0x409260000` | `0x40927ffff` | `0x20000` | [`/arm-io/dart-scaler`](../devicetree/root__arm-io__dart-scaler.md) | 0 | AppleT8110DART |
| `0x4092a0000` | `0x4092a3fff` | `0x4000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 6 | AppleM2ScalerCSCDriver |
| `0x4092c0000` | `0x4092fffff` | `0x40000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 4 | AppleM2ScalerCSCDriver |
| `0x409340000` | `0x40957bfff` | `0x23c000` | [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | 5 | AppleM2ScalerCSCDriver |
| `0x40e000000` | `0x40fff3fff` | `0x1ff4000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | 3 | AppleASCWrapV8ANE |
| `0x40f040000` | `0x40f04bfff` | `0xc000` | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) ⚠ overlaps previous | 0 | AppleT8110DART |
| `0x40f050000` | `0x40f053fff` | `0x4000` | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) ⚠ overlaps previous | 4 | AppleT8110DART |
| `0x40f060000` | `0x40f06bfff` | `0xc000` | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) ⚠ overlaps previous | 1 | AppleT8110DART |
| `0x40f080000` | `0x40f08bfff` | `0xc000` | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) ⚠ overlaps previous | 2 | AppleT8110DART |
| `0x40f0a0000` | `0x40f0abfff` | `0xc000` | [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) ⚠ overlaps previous | 3 | AppleT8110DART |
| `0x40f118000` | `0x40f11bfff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 56 | AppleEventLogHandler |
| `0x40f154000` | `0x40f157fff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 24 | AppleT8160PMGR |
| `0x40f158000` | `0x40f15bfff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 25 | AppleT8160PMGR |
| `0x40f158000` | `0x40f15bfff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 39 | AppleT8160PMGR |
| `0x40f16c000` | `0x40f16ffff` | `0x4000` | [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) ⚠ overlaps previous | 26 | AppleT8160PMGR |
| `0x40f850000` | `0x40f853fff` | `0x4000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) ⚠ overlaps previous | 1 | AppleASCWrapV8ANE |
| `0x40fe00000` | `0x40fe73fff` | `0x74000` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) ⚠ overlaps previous | 0 | AppleASCWrapV8ANE |
| `0x412000000` | `0x413ff3fff` | `0x1ff4000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | 3 | AppleASCWrapV8ANE |
| `0x413040000` | `0x41304bfff` | `0xc000` | [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) ⚠ overlaps previous | 0 | AppleT8110DART |
| `0x413050000` | `0x413053fff` | `0x4000` | [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) ⚠ overlaps previous | 4 | AppleT8110DART |
| `0x413060000` | `0x41306bfff` | `0xc000` | [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) ⚠ overlaps previous | 1 | AppleT8110DART |
| `0x413080000` | `0x41308bfff` | `0xc000` | [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) ⚠ overlaps previous | 2 | AppleT8110DART |
| `0x4130a0000` | `0x4130abfff` | `0xc000` | [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) ⚠ overlaps previous | 3 | AppleT8110DART |
| `0x413118000` | `0x41311bfff` | `0x4000` | [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) ⚠ overlaps previous | 57 | AppleEventLogHandler |
| `0x413850000` | `0x413853fff` | `0x4000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) ⚠ overlaps previous | 1 | AppleASCWrapV8ANE |
| `0x413e00000` | `0x413e73fff` | `0x74000` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) ⚠ overlaps previous | 0 | AppleASCWrapV8ANE |
| `0x1cb0000000` | `0x1cbfffffff` | `0x10000000` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | 0 | AppleT8160PCIe |
| `0x1cb0000000` | `0x1cbfffffff` | `0x10000000` | [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) ⚠ overlaps previous | 0 | APCIECoreRCGen5PLCE |
| `0x1cb0000000` | `0x1cbfffffff` | `0x10000000` | [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) ⚠ overlaps previous | 0 | APCIECoreRCGen5PLCE |
