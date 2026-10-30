# `/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter`

iOS 27.2 dyld shared cache image. Version `2360.40.13.0.1`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`

## Objective-C: 2 classes, 0 protocols, 9 methods, 1 properties

### Class pages

Every class and protocol, with its methods: [`AppleKeyboardStateManager`](../objc/AppleKeyboardStateManager_IOHIDKeyboardFilter.md), [`StickyKeyHandler`](../objc/StickyKeyHandler_IOHIDKeyboardFilter.md)

### Classes

`AppleKeyboardStateManager`, `StickyKeyHandler`

### Properties

```
@property (T@"NSMutableSet",&,N,V_capsLockStateTable) capsLockStateTable;
```

## Strings (92)

```
HIDInitialKeyRepeat
HIDStickyKeysOn
HIDFKeyMode
ON
LockKeyDelay
%#x
HIDVirtualDevice
v8@?0
CapsLockDelayOverride
ServiceFilterDebug
alt_handler_id
VendorID
NumLockKeyboardUsageMap
HIDKeyboardModifierMappingPairs
HIDRestoreKBDState
com.apple.iohid
HIDStickyKeysShiftToggles
CapsLockLEDState
HIDKeyboardSupportsF12Eject
HIDStickyKeysDisabled
FnFunctionUsageMap
HIDCapsLockLEDDarkWakeInhibit
HIDCapsLockLEDInhibit
Src
IOHIDKeyboardFilter
CapsLockState
FnKeyMode
ProductID
HIDCapsLockState
UnifiedKeyMapping
Dst
com.apple.private.hid.client.alpha-numeric-remapping
HIDKeyboardModifierMappingDst
NoRemapping
OFF
HIDSubinterfaceID
HIDKeyboardSupportedModifiers
CapsLockDelay
Modified
Delayed
UnifiedKeyMaps
PrimaryUsage
HIDKeyRepeat
UserKeyMapping
FnKeyboardUsageMap
HIDEventServiceProperties
HIDCapsLockStateCache
HIDKeyboardModifierMappingSrc
Keyboard
LegacyKeyMaps
basic_string
HIDKeyboardSupportsDoNotDisturbKey
LocationID
HIDSlowKeysDelay
MatchScore
HIDResetStickyKeyNotification
PrimaryUsagePage
CtrlKeyboardUsageMap
Class
[%@] StickyKey DOWN 0x%x:0x%x phase 0x%x\n
[%@] StickyKey state change (5xSHIFT) to %s\n
[%@] capsLockState: %d\n
[%@] _unifiedModifiedKeyMaps[kKeyMaskCtrl] updated\n
Insufficient permissions to remap alphanumeric keys or special characters for UUID: %@\n
[%@] IOHIDKeyboardFilter::setPropertyForClient: %@  %@  %@\n
[%@] _stickyKeyToggle: %d\n
[%@] _keyRepeatInitialDelayMS: %lld\n
[%@] _userKeyMap initialized\n
[%@] _capsLockDelayOverrideMS: %d\n
[%@] _lockKeyDelayMS: %d\n
(%p) for ServiceID %@ with score %d\n
[%@] _capsLockLED: %@\n
[%@] _capsLockLEDInhibit: %d\n
createMapFromArrayOfPairs: unexpected type for dst key (expected CFNumber, got %@)\n
[%@] StickyKey UP 0x%x:0x%x phase 0x%x\n
Event dropped: %@\n
[%@] _keyRepeatDelayMS: %lld\n
[%@] Event cancelled\n
[%@] Restoring capslock state\n
[%@] _slowKeysDelayMS = %d\n
[%@] _capsLockDelayMS: %d\n
[%@] _stickyKeyOn: %d\n
[%@] StickyKey DOWN in bad state for 0x%x:0x%x\n
[%@] Set capslock state: %d client: %@\n
[%@] IOHIDKeyboardFilter::setPropertyForClient _fnKeyMode: %x %@\n
[%@] StickyKey state %x -> %x\n
[%@] updateCapslockLED:%d->%d capsLockLED:%@ capsLockState:%d client:%@, didUpdateCapsLockLEDState:%d\n
[%@] StickyKey UP in bad state for 0x%x:0x%x\n
[%@] _stickyKeyDisable: %d\n
[%@] _capsLockDarkWakeLEDInhibit: %d\n
createMapFromArrayOfPairs: unexpected type for src key (expected CFNumber, got %@)\n
[%@] _modifiersKeyMap initialized\n
```
