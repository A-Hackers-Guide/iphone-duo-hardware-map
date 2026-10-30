# `TUSplitSessionInfo`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _conversationID;
@"TUNearbyDeviceHandle" _device;
@"TUNeighborhoodHandoffContext" _handoffContext;
```

## Properties

```
@property (T@"NSUUID",R,N,V_conversationID) conversationID;
@property (T@"TUNearbyDeviceHandle",R,N,V_device) device;
@property (T@"TUNeighborhoodHandoffContext",R,N,V_handoffContext) handoffContext;
```

## Class methods

```
+[TUSplitSessionInfo supportsSecureCoding];
```

## Instance methods

```
-[TUSplitSessionInfo conversationID];
-[TUSplitSessionInfo device];
-[TUSplitSessionInfo encodeWithCoder:];
-[TUSplitSessionInfo description];
-[TUSplitSessionInfo initWithCoder:];
-[TUSplitSessionInfo handoffContext];
-[TUSplitSessionInfo initWithConversationID:device:handoffContext:];
```
