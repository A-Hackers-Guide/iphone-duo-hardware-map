# `/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`

iOS 27.2 dyld shared cache image. Version `4178.40.10.0.0`. **[DSC]**

## Linked libraries (8)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 14 classes, 9 protocols, 300 methods, 118 properties

### Class pages

Every class and protocol, with its methods: [`CAMAbstractOverlayServiceControl`](../objc/CAMAbstractOverlayServiceControl_CameraOverlayServices.md), [`CAMOverlayBooleanRange`](../objc/CAMOverlayBooleanRange_CameraOverlayServices.md), [`CAMOverlayClientInterface`](../objc/CAMOverlayClientInterface_CameraOverlayServices.protocol.md), [`CAMOverlayContinuousFloatRange`](../objc/CAMOverlayContinuousFloatRange_CameraOverlayServices.md), [`CAMOverlayDiscreteFloatRange`](../objc/CAMOverlayDiscreteFloatRange_CameraOverlayServices.md), [`CAMOverlayDiscreteValueRange`](../objc/CAMOverlayDiscreteValueRange_CameraOverlayServices.protocol.md), [`CAMOverlayFloatValueRange`](../objc/CAMOverlayFloatValueRange_CameraOverlayServices.protocol.md), [`CAMOverlayIndexedRange`](../objc/CAMOverlayIndexedRange_CameraOverlayServices.md), [`CAMOverlayServerInterface`](../objc/CAMOverlayServerInterface_CameraOverlayServices.protocol.md), [`CAMOverlayService`](../objc/CAMOverlayService_CameraOverlayServices.md), [`CAMOverlayServiceConnection`](../objc/CAMOverlayServiceConnection_CameraOverlayServices.md), [`CAMOverlayServiceControl`](../objc/CAMOverlayServiceControl_CameraOverlayServices.md), [`CAMOverlayServiceControlUpdate`](../objc/CAMOverlayServiceControlUpdate_CameraOverlayServices.md), [`CAMOverlayServicePicker`](../objc/CAMOverlayServicePicker_CameraOverlayServices.md), [`CAMOverlayServiceSlider`](../objc/CAMOverlayServiceSlider_CameraOverlayServices.md), [`CAMOverlayServiceSpecification`](../objc/CAMOverlayServiceSpecification_CameraOverlayServices.md), [`CAMOverlayServiceToggle`](../objc/CAMOverlayServiceToggle_CameraOverlayServices.md), [`CAMOverlayTitleRange`](../objc/CAMOverlayTitleRange_CameraOverlayServices.md), [`CAMOverlayValueRange`](../objc/CAMOverlayValueRange_CameraOverlayServices.protocol.md), [`NSCoding`](../objc/NSCoding_CameraOverlayServices.protocol.md), [`NSCopying`](../objc/NSCopying_CameraOverlayServices.protocol.md), [`NSObject`](../objc/NSObject_CameraOverlayServices.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_CameraOverlayServices.protocol.md)

### Classes

`CAMAbstractOverlayServiceControl`, `CAMOverlayBooleanRange`, `CAMOverlayContinuousFloatRange`, `CAMOverlayDiscreteFloatRange`, `CAMOverlayIndexedRange`, `CAMOverlayService`, `CAMOverlayServiceConnection`, `CAMOverlayServiceControl`, `CAMOverlayServiceControlUpdate`, `CAMOverlayServicePicker`, `CAMOverlayServiceSlider`, `CAMOverlayServiceSpecification`, `CAMOverlayServiceToggle`, `CAMOverlayTitleRange`

### Protocols

`CAMOverlayClientInterface`, `CAMOverlayDiscreteValueRange`, `CAMOverlayFloatValueRange`, `CAMOverlayServerInterface`, `CAMOverlayValueRange`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R,N) count;
@property (Td,R,N) minimum;
@property (Td,R,N) maximum;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (Tq,R,N,V_controlType) controlType;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",R,N,V_imageName) imageName;
@property (TB,R,N,V_persistentlyVisible) persistentlyVisible;
@property (TQ,R,N) count;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,V_minimum) minimum;
@property (Td,R,N,V_maximum) maximum;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,C,N,V__explicitStorage) _explicitStorage;
@property (Td,R,N,V__implicitStep) _implicitStep;
@property (TQ,R,N,V_count) count;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,V_minimum) minimum;
@property (Td,R,N,V_maximum) maximum;
@property (T@"NSArray",R,C,N,V__titles) _titles;
@property (TQ,R,N,V_count) count;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CAMOverlayServiceConnection",&,N,S_setActiveConnection:,V__activeConnection) _activeConnection;
@property (TQ,N,S_setStatus:,V_status) status;
@property (T@"BSServiceConnection",&,N,S_setServerConnection:,V__serverConnection) _serverConnection;
@property (T@"<CAMOverlayServerInterface>",&,N,S_setServerProxy:,V__serverProxy) _serverProxy;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__connectionQueue) _connectionQueue;
@property (TB,N,S_setLastKnownOverlayVisibility:,V__lastKnownOverlayVisibility) _lastKnownOverlayVisibility;
@property (TB,N,S_setLastKnownOverlayInterfaceReduced:,V__lastKnownOverlayInterfaceReduced) _lastKnownOverlayInterfaceReduced;
@property (TB,N,S_setLastKnownFocusLocked:,V__lastKnownFocusLocked) _lastKnownFocusLocked;
@property (T@"<CAMOverlayServiceConnectionClient>",R,W,N,V_client) client;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_clientQueue) clientQueue;
@property (TB,N,V_focusLockGestureEnabled) focusLockGestureEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_captureDeviceUniqueID) captureDeviceUniqueID;
@property (Tq,N,V_captureDeviceProperty) captureDeviceProperty;
@property (T@"<CAMOverlayValueRange>",&,N,V_valueRange) valueRange;
@property (T@"NSString",&,N,V_valueFormat) valueFormat;
@property (T@"CAMOverlayDiscreteFloatRange",&,N,V_primaryValues) primaryValues;
@property (T@"NSString",&,D,N) imageName;
@property (T@"NSString",&,D,N) title;
@property (Tq,N,V_rangeScale) rangeScale;
@property (T@"NSString",R,N,V_controlIdentifier) controlIdentifier;
@property (Tq,R,N,V_valueType) valueType;
@property (Tf,R,N,V_floatValue) floatValue;
@property (Tq,R,N,V_indexValue) indexValue;
@property (T@"NSDictionary",R,N,V_styleDictionary) styleDictionary;
@property (TB,R,N,V_booleanValue) booleanValue;
@property (TB,R,N,GisRecording,V_recording) recording;
@property (TB,R,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N,GisValueUpdate) valueUpdate;
@property (Tq,R,N,V_pickerType) pickerType;
@property (T@"NSString",R,N,V_captureSessionUniqueID) captureSessionUniqueID;
@property (T@"NSArray",R,N,V_valueTitles) valueTitles;
@property (Tq,R,N,V_sliderType) sliderType;
@property (T@"<CAMOverlayFloatValueRange>",R,N,V_valueRange) valueRange;
@property (T@"NSDictionary",&,N,V_displayValuesByValue) displayValuesByValue;
@property (T@"NSString",R,N,V_captureDeviceUniqueID) captureDeviceUniqueID;
@property (T@"NSString",R,N,V_captureSessionUniqueID) captureSessionUniqueID;
@property (T@"CAMOverlayDiscreteFloatRange",R,N,V_primaryValues) primaryValues;
@property (Tq,R,N,V_rangeScale) rangeScale;
@property (T@"NSString",C,N,V_valueFormat) valueFormat;
@property (Tq,R,N,V_toggleType) toggleType;
@property (T@"NSString",&,N,V_onImageName) onImageName;
@property (T@"NSString",&,N,V_offImageName) offImageName;
@property (T@"NSString",R,N,V_onTitle) onTitle;
@property (T@"NSString",R,N,V_offTitle) offTitle;
@property (T@"NSArray",R,C,N,V__titles) _titles;
@property (T@"CAMOverlayIndexedRange",R,N) indexedRange;
@property (TQ,R,N) count;
@property (TQ,R,N) valueType;
@property (TQ,R,N) rangeType;
@property (TB,R,N,GisFloatingPoint) floatingPoint;
@property (TB,R,N,GisDiscrete) discrete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (152)

```
DISABLED
float
camera.aperture
v32@?0@\"NSNumber\"8Q16^B24
systemOverlay.halfPressGestureEnabled
Settings
lock.fill
offTitle
Toggle
valueType
, 
<%@ %p; %lu values; min: %.3f; max: %.3f; step: %.3f>
identifier
Systematic
recording
<%@ %p; min: %.3f; max: %.3f>
index
<%@ %p; %lu values: %@>
<%@ %p; %lu values>
primaryValues
lock.open.fill
%.3f
_explicitStorage
Tostada
PoREventRouting
Inactive
Invalid
TONE_TEXT
onTitle
v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8
com.apple.Accessibility
v8@?0
enabled
<%@: %p: %@ %@>
PICKER_STYLE
B32@?0@\"NSNumber\"8Q16^B24
%@.%@
style
maximum
CameraButtonSensitivity
com.apple.CameraOverlayAngel
Core
com.apple.camera.overlay-connection
InvalidValueType
ZOOM_FACTOR_TEXT
<%@: %p; %@ \"%@\"; ID: %@>
ENABLED
rangeScale
SLIDER_STYLE_TONE
dot.grid.bottomrighthalf.app
sliderType
displayValuesByValue
invalid
InvalidValue
1
indexValue
SLIDER_STYLE_INTENSITY
captureDeviceUniqueID
%@
_titles
YES
Slider
v16@?0@\"<BSXPCEncoding>\"8
CAMOverlayService
TostadaUI
systemOverlay.lastUsedControl
InvalidIdentifier
toggleType
TostadaRemoteUI
captureDeviceProperty
systemOverlay.swipeToPresentEnabled
%@(%@)
valueTitles
captureSessionUniqueID
q24@?0@\"NSNumber\"8@\"NSNumber\"16
com.apple.CameraOverlayAngel.application-service
plusminus
TOGGLE_OFF
imageName
Client
systemOverlay.hidesClientControls
pickerType
SLIDER_EXPOSURE
TOGGLE_ON
count
CameraButtonCapability
booleanValue
dot.dot.grid.app
swirl.circle.righthalf.filled
Automatic
com.apple.camera
SLIDER_ZOOM
<%@ %p>
controlIdentifier
CameraOverlayServices
crosshair.viewfinder
SLIDER_STYLE_COLOR
onImageName
valueFormat
boolean
test
valueRange
systemOverlay.menuToggleMaxIntervalMilliseconds
%f
floatValue
i
lifepreserver
title
NO
com.apple.camera.overlay
Programmatic
InvalidConnection
SLIDER_LENS
minimum
Active
EXPOSURE_BIAS_TEXT
offImageName
Picker
styleDictionary
v16@?0@\"<BSServiceConnectionConfiguring>\"8
InactiveConnection
%ld
com.apple.CameraOverlayAngel.client-app-service
CAMOverlayErrorDomain
CAMUserPreferenceCameraAdjustmentsEnabled
 ... %.3f
_implicitStep
Not sending overlay value %{public}@ for ID %{public}@: %{public}@
Received overlay focusLocked %{public}@
Enabling camera adjustments by default due to last-used control data: %@
Lookup failed for machName/service %{public}@/%{public}@.
Overlay service connection became %{public}@ for reason %{public}@
Received overlay update %{public}@ for ID %{public}@
Disabling camera adjustments by default due to lack of usage history
Failed to unarchive camera control settings: %{public}@
Invalid value format %{public}@ for %{public}@: %@
Activating new overlay service connection
Sending overlay value %{public}@ for ID %{public}@
Received overlay visibility %{public}@ for control ID %{public}@
Received overlay interfaceReduced %{public}@
Inspecting defaults for Camera Control usage history
Disabling camera adjustments by default due to nil data
Disabling camera adjustments by default due to disabled gestures
Enabling camera adjustments by default due to explicitly enabled gestures
Not sending overlay controls: %{public}@
Sending overlay %lu control(s)
Sending overlay focus-lock gesture %{public}@
Received active control ID %{public}@
Could not find CameraOverlayAngel bundle record: %{public}@
Failed to archive camera control settings: %{public}@
Could not find CameraOverlayAngel bundle record for setting last used control: %{public}@
Enabling camera adjustments by default due to behavior defaults written
```
