# `/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`

iOS 27.2 dyld shared cache image. Version `14.0.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/HID.framework/HID`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 4 classes, 0 protocols, 59 methods, 16 properties

### Class pages

Every class and protocol, with its methods: [`AHFManager`](../objc/AHFManager_AppleHIDFeedback.md), [`AHFPencilController`](../objc/AHFPencilController_AppleHIDFeedback.md), [`AHFPencilPatternLibrary`](../objc/AHFPencilPatternLibrary_AppleHIDFeedback.md), [`AHFTrackpadController`](../objc/AHFTrackpadController_AppleHIDFeedback.md)

### Classes

`AHFManager`, `AHFPencilController`, `AHFPencilPatternLibrary`, `AHFTrackpadController`

### Properties

```
@property (T@"AHFTrackpadController",&,N,V_trackpadController) trackpadController;
@property (T@"AHFPencilController",&,N,V_pencilController) pencilController;
@property (T@"AHFPencilPatternLibrary",&,N,V_patternsLibrary) patternsLibrary;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_prevTimestampUs) prevTimestampUs;
@property (T@"HIDEventSystemClient",&,N,V_digitizerStylusClient) digitizerStylusClient;
@property (T@"NSMutableSet",&,N,V_availableDigitizerStylus) availableDigitizerStylus;
@property (T@"HIDEventSystemClient",&,N,V_opaqueTouchClient) opaqueTouchClient;
@property (T@"NSMutableSet",&,N,V_availableOpaqueTouch) availableOpaqueTouch;
@property (T@"HIDEventSystemClient",&,N,V_pencilHapticsClient) pencilHapticsClient;
@property (TI,N,V_availablePencilHaptics) availablePencilHaptics;
@property (T@"NSDictionary",&,N,V_library) library;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_prevTimestampUs) prevTimestampUs;
@property (T@"HIDEventSystemClient",&,N,V_trackpadClient) trackpadClient;
@property (T@"NSMutableDictionary",&,N,V_availableTrackpads) availableTrackpads;
```

## Strings (110)

```
ActuationSupported
context_menu
-[AHFPencilPatternLibrary createPatternsLibraryFrom:]
com.apple.hid.AppleHIDFeedback
Could not find pattern %@
v16@?0@\"HIDServiceClient\"8
drag_drop_table_edit
/AppleInternal/Library/Application Support/AppleHIDFeedback/Patterns/Pencil
Could not retrieve power sources for accessories
-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke
-[AHFPencilController playFeedback:accessoryID:timestamp:error:]
detent_out
Spacing
com.apple.hid.AppleHIDFeedback.Pencil
IOClass
-[AHFPencilController initializePencilHapticsSystem]_block_invoke
PhysicalDeviceUniqueID
-[AHFTrackpadController playFeedbackGated:client:timestamp:error:]
Num Loops
Too soon after previous haptic (delta %lluus)
Framework
edge
empty_app_switcher
MGCopyAnswer
PrimaryUsagePage
HapticsMessage
com.apple.hid.AppleHIDFeedback.Trackpad
-[AHFTrackpadController initializeTrackpadSystem]_block_invoke
MicroTap
Trackpad
state
-[AHFTrackpadController playFeedback:senderID:timestamp:error:]
pattern
pathExtension == %@
Type
IOService
-[AHFPencilPatternLibrary maybeGetExploratoryPayload:]
Pencil
-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke
-[AHFPencilController playFeedback:senderID:timestamp:error:]
SenderID 0x%llX not found
-[AHFPencilPatternLibrary init]
Power source category %@ not supported
Error requesting playback to kernel: %s
app_switcher
Q
Timeout
PrimaryUsage
-[AHFPencilController playFeedbackGated:haptics:timestamp:error:]
SerialNumber
MiniTap
Gain
/usr/lib/libMobileGestalt.dylib
InternalBuild
refresh
Could not retrieve power sources list for accessories
Power source with ID %@ not found
generic_selection
Patterns/Pencil
B32@?0@8@16^B24
v8@?0
Accessory Identifier
AppleEmbeddedBluetoothHaptics
Accessory ID %@ not found
index_bar_selection
AppKitActuateWithID
WideTap
Pattern
detent_in
Error requesting playback of actuation ID %d to service
-[AHFTrackpadController playFeedback:accessoryID:timestamp:error:]
Priority
Power Source ID
Accessory Category
i
No Pencil Haptics device to play pattern %@ to
page_control_selection
%s Could not find a 'Type' in asset %u in %@
%s Could not understand 'Type' in asset %u in %@
%s Correctly added pattern '%@' (%@) to library (priority=%@, timeout=%@): %@
%s Loaded %lu haptics patterns: %@
%s Could not find a 'Timeout' in %@
%s \\Array 'Pattern' is empty in %@
%s Trying to play pattern %@ on pencil power source accessory ID %@
%s Pattern '%@' already exists in library. Overriding
%s Could load %@
%s Could not find a 'Priority' in %@
%s Trying to play pattern %@ on pencil HID sender ID 0x%llX
%{public, signpost.description:begin_time}llu
%s Could not find a 'Num Loops' in %@ or number of loops invalid (0)
%s Pattern '%@' is a exploratory '%@' with gain %u
%s Trackpad with senderID 0x%llx added in %s queue
%s Trying to play pattern %@ on trackpad HID sender ID 0x%llX
%s Could not find a 'Pattern' in %@
%s Pencil Haptics with senderID 0x%llx removed in %s queue
PlayPencilFeedback
%s Trackpad with senderID 0x%llx removed in %s queue
%s The following haptics patterns are being overriden: %@
%s Could not find a name for pattern in %@
%s Digitizer Stylus with senderID 0x%llx added in %s queue
%s OpaqueTouch with senderID 0x%llx added in %s queue
%s Could not find a 'Gain' in asset %u in %@
%s Invalid value for 'Gain' in asset %u in %@
%s Trying to play pattern %@ on trackpad power source accessory ID %@
%s Loaded %lu internal haptics patterns: %@
%s Could not find a 'Spacing' in asset %u in %@
%s Digitizer Stylus with senderID 0x%llx removed in %s queue
%s OpaqueTouch with senderID 0x%llx removed in %s queue
%s Pencil Haptics with senderID 0x%llx added in %s queue
%s Playing pattern %@ requested %lldus ago, previous was %.2fms ago
```
