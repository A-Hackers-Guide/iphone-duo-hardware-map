# `/usr/lib/libenergytrace.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 69,600 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1544)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/libenergytrace.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (12)

```
EnTr_Activation_Begin
EnTr_Activation_Modify
parent_component = %{public}u                                              parent_opcode = %{public, signpost.description:attribute}u sub_component = %{public}u sub_opcode = %{public}u sub_activation_id = %{public}lu
EnTr_Activation_Associate
EnTr_Activation_End
act_opcode = %{public, signpost.description:attribute}u act_quality = %{public}u act_value = %{public}lld 
com.apple.EnergyTracing
EnTr_AppState
EnTr_SysPower
EnTr_Networking
EnTr_Spatial
v8@?0
```
