# `/System/Library/PrivateFrameworks/HID.framework/HID`

iOS 27.2 dyld shared cache image. Version `2360.40.13.0.1`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

## Objective-C: 24 classes, 1 protocols, 248 methods, 39 properties

### Class pages

Every class and protocol, with its methods: [`HIDBasicTimeSync`](../objc/HIDBasicTimeSync_HID.md), [`HIDEventSystemClient`](../objc/HIDEventSystemClient_HID.md), [`HIDLibElement`](../objc/HIDLibElement_HID.md), [`HIDManager`](../objc/HIDManager_HID.md), [`HIDTimeSync`](../objc/HIDTimeSync_HID.md), [`HIDTransaction`](../objc/HIDTransaction_HID.md), [`HIDUserDevice`](../objc/HIDUserDevice_HID.md), [`HIDVirtualEventService`](../objc/HIDVirtualEventService_HID.md), [`IOHIDDeviceClass`](../objc/IOHIDDeviceClass_HID.md), [`IOHIDIUnknown2`](../objc/IOHIDIUnknown2_HID.md), [`IOHIDObsoleteDeviceClass`](../objc/IOHIDObsoleteDeviceClass_HID.md), [`IOHIDObsoleteQueueClass`](../objc/IOHIDObsoleteQueueClass_HID.md), [`IOHIDOutputTransactionClass`](../objc/IOHIDOutputTransactionClass_HID.md), [`IOHIDPlugin`](../objc/IOHIDPlugin_HID.md), [`IOHIDQueueClass`](../objc/IOHIDQueueClass_HID.md), [`IOHIDTransactionClass`](../objc/IOHIDTransactionClass_HID.md), [`NSCopying`](../objc/NSCopying_HID.protocol.md)

### Classes

`HIDBasicTimeSync`, `HIDConnection`, `HIDDevice`, `HIDElement`, `HIDEvent`, `HIDEventService`, `HIDEventSystemClient`, `HIDLibElement`, `HIDManager`, `HIDServiceClient`, `HIDSession`, `HIDTimeSync`, `HIDTransaction`, `HIDUserDevice`, `HIDVirtualEventService`, `IOHIDDeviceClass`, `IOHIDIUnknown2`, `IOHIDObsoleteDeviceClass`, `IOHIDObsoleteQueueClass`, `IOHIDOutputTransactionClass`, `IOHIDPlugin`, `IOHIDQueueClass`, `IOHIDTransactionClass`, `NSError`

### Protocols

`NSCopying`

### Properties

```
@property (T@"NSArray",R) services;
@property (T^{__IOHIDElement=},V_element) elementRef;
@property (T^{__IOHIDValue=}) valueRef;
@property (T^{__IOHIDValue=},V_defaultValue) defaultValueRef;
@property (Tq) integerValue;
@property (T@"NSData") dataValue;
@property (T@"NSString",C,V_psKey) psKey;
@property (TQ,R) timestamp;
@property (Tq,R) length;
@property (T{IOHIDElementStruct=IIIIIIIIIiiiiIIIIIIIIIII},R,V_elementStruct) elementStruct;
@property (TB,V_isConstant) isConstant;
@property (TB,V_isUpdated) isUpdated;
@property (TI,R) elementCookie;
@property (TI,R) collectionCookie;
@property (Ti,R) type;
@property (TI,R) usage;
@property (TI,R) usagePage;
@property (TI,R) unit;
@property (TC,R) unitExponent;
@property (TC,R) reportID;
@property (TI,R) usageMin;
@property (TI,R) usageMax;
@property (Ti,R) collectionType;
@property (T@"NSArray",R) devices;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@?,R,N,V_eventHandler) eventHandler;
@property (T@?,R,N,V_cancelHandler) cancelHandler;
@property (TI,N) state;
@property (Tq) direction;
@property (TI,R) service;
@property (T@"HIDEventSystemClient",&,V_client) client;
@property (T@"HIDServiceClient",&,V_serviceClient) serviceClient;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (TQ,R) serviceID;
@property (T@"<HIDVirtualEventServiceDelegate>",W,V_delegate) delegate;
@property (TI,R,V_port) port;
@property (T^{__CFRunLoopSource=},R,V_runLoopSource) runLoopSource;
@property (TI,R,V_connect) connect;
@property (TI,R,V_service) service;
```

## Strings (454)

```
DuplicateIndex
isRelative
translationZ
compassX
monitorForCurrentProcess
media is not formatted
ScaledMax
rosetta_convert_to_rosetta_absolute_time
forceStage
pointerButtonMask
vendorDefinedUsage
forceStagePressure
scrollIsPixels
dockSwipeMotion
TimeSyncEnabled
forceStageNormalizedForceVelocity
gyroZ
keyboardSlowKeyPhase
Transport
assertion failure: Unimplemented in base class
device is busy
v8@?0
digitizerMinorRadius
digitizerIrregularity
dockSwipePositionX
assertion failure: Set report handler already set
DMA failure
ElementCookie
accelerometerSubType
heartRateGenerationCount
collectionUsagePage
gyroX
fluidTouchGesturePositionY
assertion failure: Input report handler already set
assertion failure: Event handler already set
device is write locked
injected
progressEventType
buttonNumber
navigationSwipePositionY
orientationOrientationType
%@
device is not open
no DMA frames enqueued
vendorDefinedUsagePage
digitizerPressure
device is read locked
IsArray
Unit
gyroY
IOClass
UnitExponent
gameControllerDirectionPadRight
multiAxisPointerRx
velocityZ
unsupported mode
interpolated
compassZ
device is exclusive access
progressLevel
keyboardDown
HIDUserDeviceCreateInactive
device is offline
gameControllerType
gameControllerFaceButtonY
navigationSwipeProgress
keyboardClickSpeed
digitizerIsDisplayIntegrated
digitizerDensity
orientationTiltY
DeviceUsagePairs
ambientLightSensorRawChannel3
heartRateLocation
forceStageReleasedThreshold
gameControllerFaceButtonX
gyroSubType
fluidTouchGestureProgress
isIdentifiedGame
powerSubType
forceProgress
multiAxisPointerButtonMask
gyroType
gyroSequence
keyboardStickyKeyPhase
pointerZ
media is not present
ambientLightColorComponent2
touchSensitiveButtonMinorRadius
motionGestureGestureType
com.apple.hid.queueUsage
!Ta
ambientLightSensorLevel
digitizerTwist
keyboardRepeat
IOHIDDeviceSuspend
ambientLightColorComponent0
touchSensitiveButtonUsagePage
dynamicButtonReleaseThreshold
dynamicButtonConfigurationGeneration
multiAxisPointerX
unicodeLength
Max
hingeAngleVelocityDegreesPerSecond
dynamicButtonPadID
dynamicButtonTransition
gameControllerJoyStickAxisZ
gameControllerShoulderButtonR1
multiAxisPointerZ
boundaryScrollFlavor
orientationQuatX
digitizerAuxiliaryPressure
navigationSwipePositionZ
scrollX
keyboardUsage
keyboardMouseKeyToggle
isApprovedCarPlayDeviceHIDRMDeviceState
internal driver error
device is not responding
dynamicButtonConfigurationID
humidityRH
assertion failure: Cancel Handler cannot be set after HIDManager is activated
IOHIDDeviceClass
Usage
UsagePage
IsWrapping
DeviceOpenedByEventSystem
scaleY
digitizerTiltX
compassType
navigationSwipePositionX
biometricTapCount
orientationDeviceOrientationUsage
orientationQuatZ
genericGestureTypeSwipeProgress
isPixelUnits
compassSubType
navigationSwipeFlavor
scrollZ
unicodeEncoding
assertion failure: Removal handler already set
general error
vendorDefinedData
symbolicHotKeyValue
touchSensitiveButtonEventMask
powerType
digitizerAltitude
boundaryScrollMask
dockSwipeProgress
keyboardLongPress
MatchingEvent
heartRateRate
touchSensitiveButtonTouch
forceStageNormalizedForce
buttonClickCount
boundaryScrollProgress
orientationQuatY
queueType
touchSensitiveButtonMajorRadius
currentBrightness
boundaryScrollMotion
resource shortage
no interrupt attached
unanticipated driver error
Min
ElementCookieMax
translationX
multiAxisPointerRy
buttonPressure
navigationSwipeMask
unicodeQuality
assertion failure: Cancel handler set after HIDEventSystemClient was activated
assertion failure: Filter handler already set
device is without power
fluidTouchGestureMotion
dockSwipeMask
unicodePayload
success
device is not readable
device is still open
IsNonLinear
rosetta_is_current_process_translated
!
touchSensitiveButtonUsage
touchSensitiveButtonNormalizedPositionDeltaX
gameControllerFaceButtonB
navigationSwipeMotion
I/O error
ambientLightColorComponent1
forceBehavior
gameControllerButtonM3
orientationAzimuth
proximityDetectionMask
probabilityLevel
fluidTouchGestureMask
Type
lEDState
collectionUngroupForLegacy
EventType
accelerometerSequence
gameControllerButtonR4
transitionTime
lEDMask
assertion failure: Reset handler already set
temperatureLevel
accelerometerType
fluidTouchGestureFlavor
pointerY
memory allocation error
Built-In
HasNullState
v32@?0@\"NSString\"8@\"NSNumber\"16^B24
gameControllerFaceButtonA
dockSwipeFlavor
keyboardUsagePage
/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy
assertion failure: Input element handler already set
I/O timeout
data overrun
gameControllerDirectionPadUp
hingeAngleAngleDegrees
dynamicButtonUsage
cannot acquire lock
HIDFramework
IsRelative
dynamicButtonNextThreshold
dynamicButtonUsagePage
forceStagePressedThreshold
digitizerType
multiAxisPointerY
IOGeneralInterest
staticSize
MaxInputReportSize
isCenterOrigin
dynamicButtonPositionID
digitizerButtonMask
digitizerQuality
assertion failure: Device has already been activated/cancelled.
assertion failure: Get report handler already set
-
invalid argument
dynamicButtonPositionY
dynamicButtonForce
dynamicButtonThreshold
boundaryScrollPositionX
TSClockID
privilege violation
bad IPC message ID
device/channel is not attached
translationY
digitizerGenerationCount
velocityX
unsupported function
no completion routine
0x%x unknown
UniqueID
ElementCookieMin
scaleX
gameControllerButtonL4
gameControllerButtonM1
digitizerRange
digitizerX
orientationAltitude
proximityProximityType
/usr/lib/libRosetta.dylib
ambientLightSensorRawChannel1
gameControllerButtonM4
digitizerChildEventMask
digitizerWillUpdateMask
digitizerMajorRadius
Q
ScaledMin
vendorDefinedDataLength
hingeAngleState
ambientLightSensorRawChannel2
rotationY
humiditySequence
dockSwipePositionY
keyboardPressCount
<HIDVirtualEventService serviceID:0x%llx>
digitizerOrientationType
rotationX
PrimaryUsage
#
v24@?0@\"GPProcessMonitor\"8@\"GPProcessInfo\"16
HIDTimeSyncProperties
device port already exists
operation was aborted
gameControllerShoulderButtonL2
compassY
orientationTiltZ
operation is not permitted
vendorDefinedVersion
atmosphericPressureLevel
virtual memory error
element: %p type: %d uP: 0x%02x u: 0x%02x cookie: %d val: %ld
genericGestureType
gameControllerShoulderButtonR2
gameControllerThumbstickButtonRight
digitizerCollection
digitizerTouch
assertion failure: property change handler already set
assertion failure: Property changed notification handler already set
hingeAngleMechanicalAngleDegrees
touchSensitiveButtonNormalizedPositionX
biometricUsage
lEDNumber
deviceQueue
+
no space for data
device error
assertion failure: IOHIDEventSystem does not exist
scaleZ
symbolicHotKeyIsCGSEvent
ambientLightSensorColorTemperature
forceStageTransition
atmosphericSequence
MaxReportBufferCount
collectionUsage
digitizerY
boundaryScrollPositionY
no such device
Size
powerMeasurement
digitizerIdentity
digitizerTiltY
rotationZ
dockSwipePositionZ
pointerX
IOHIDDevice
device is not ready
assertion failure: Invalid object: instance is not a virtual event service
accelerometerX
heartRateConfidence 
gameControllerThumbstickButtonLeft
biometricUsagePage
I
no DMA channels available
cannot wire physical memory
accelerometerY
ambientLightSensorIlluminance
gameControllerDirectionPadDown
gameControllerJoyStickAxisRz
digitizerAzimuth
biometricEventType
PrimaryUsagePage
usagePairs
keyboardStickyKeyToggle
i
IOHIDDeviceForceInterfaceRematch
ReportSize
HasPreferredState
UsageMin
UsageMax
digitizerIndex
fluidTouchGesturePositionX
ReportID
ReportCount
touchSensitiveButtonNormalizedPositionY
digitizerZ
digitizerEventMask
digitizerQualityRadiiAccuracy
orientationRadius
HIDTimeSyncProtocol
IOService
rld failure
GPProcessMonitor
assertion failure: Service notification handler already set
media error
gameControllerJoyStickAxisY
multiAxisPointerRz
buttonState
biometricLevel
orientationTiltX
message is too large
forceStageStage
gameControllerButtonM2
transport
assertion failure: Device notification handler already set
CollectionCookie
digitizerRoll
compassSequence
motionActivityActivityType
UsagePercent
device is not writeable
bus bandwidth would be exceeded
ReportBufferEntrySize
accelerometerZ
isCollection
dynamicButtonStageID
forceStageNextThreshold
gameControllerDirectionPadLeft
gameControllerJoyStickAxisX
motionActivityConfidence
BLETimesyncInfo
ambientLightSensorRawChannel0
ambientLightColorSpace
motionGestureProgress
digitizerDidUpdateMask
buttonMask
scrollY
assertion failure: Failed to setPropertyChangeHandler, dispatch queue not set
timestamp: %llu type: %ld usagePage: %ld usage: %ld reportID: %ld value: %ld
MatchingEventOptions
genericGestureTypeTapCount
targetBrightness
orientationQuatW
proximityLevel
Mach IPC failure
alignment error
ambientLightDisplayBrightnessChanged
isBuiltIn
touchSensitiveButtonNormalizedPositionDeltaY
gameControllerShoulderButtonL1
velocityY
Active
data underrun
IOServiceOpen failed: 0x%x\n
assertion failure: \"_state == HIDTimeSyncStateInit\" -> %llu
setValue(%#llx):%#x\n
kIOHIDLibUserClientUpdateElementValues(%#llx):%#x\n
Unable to create queue analytics\n
assertion failure: \"_eventHandler\" -> %llu
assertion failure: Invalid dispatch state: 0x%x
W2 btclk(ns):%llu local abs:%llu Synced ts:%llu remote->local latency(ns):%s%llu
IOHIDDeviceClass failed to retain service object with err %x\n
kIOHIDLibUserClientResumeReports:%#x\n
Failed find device for ID 0x%llx
Unsupported matching criteria: %@ %@\n
Unable to copy back value for element, unexpected cookie(%ld) expected:%d\n
assertion failure: \"_queue\" -> %llu
handleActivate enabling TS failed
IOConnectCallMethod(kIOHIDLibUserClientGetElements):%x\n
Failed to create queue\n
assertion failure: Unknown matching criteria: %@
Failed to get service for ID 0x%llx
Couldn't create TSUserFilteredClock!
getValue(%#llx):%#x\n
Failed to set up property notifications: 0x%x
assertion failure: \"_state & HIDTimeSyncStateActivate\" -> %llu
Failed to get matching for ID 0x%llx
kIOHIDLibUserClientPostElementValues(%llx):%x\n
kIOHIDLibUserClientPostElementValues(%#llx):%#x\n
Unable to copy back value for element, unexpected size(%d)\n
TimeSync: not locked, clockID: 0x%llx state: %d
IOConnectCallMethod(kIOHIDLibUserClientGetElementCount):%x\n
Device is seized, reports will be dropped until the seizing client closes\n
IOConnectCallMethod(kIOHIDLibUserClientOpen):%x\n
assertion failure: Invalid dispatch state: %d
Failed to create IOHIDQueue plugin result: 0x%x\n
Failed to create iterator for ID 0x%llx
IOServiceAddInterestNotification 0x%x
Failed to map memory: 0x%x\n
assertion failure: \"self.state == HIDTimeSyncStateActivate\" -> %llu
handleCancel disabling TS failed
```
