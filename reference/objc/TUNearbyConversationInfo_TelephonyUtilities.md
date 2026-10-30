# `TUNearbyConversationInfo`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _conversationUUID;
@"NSString" _userProfileIdentifier;
@"TUNearbyDeviceHandle" _deviceHandle;
Q _avMode;
@"NSSet" _supportedHandoffTypes;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_conversationUUID) conversationUUID;
@property (T@"NSString",R,C,N,V_userProfileIdentifier) userProfileIdentifier;
@property (T@"TUNearbyDeviceHandle",R,C,N,V_deviceHandle) deviceHandle;
@property (TQ,R,N,V_avMode) avMode;
@property (T@"NSSet",R,C,N,V_supportedHandoffTypes) supportedHandoffTypes;
```

## Class methods

```
+[TUNearbyConversationInfo supportsSecureCoding];
```

## Instance methods

```
-[TUNearbyConversationInfo conversationUUID];
-[TUNearbyConversationInfo encodeWithCoder:];
-[TUNearbyConversationInfo hash];
-[TUNearbyConversationInfo description];
-[TUNearbyConversationInfo initWithCoder:];
-[TUNearbyConversationInfo copyWithZone:];
-[TUNearbyConversationInfo isEqual:];
-[TUNearbyConversationInfo avMode];
-[TUNearbyConversationInfo deviceHandle];
-[TUNearbyConversationInfo initWithConversationUUID:userProfileIdentifier:deviceHandle:avMode:supportedHandoffTypes:];
-[TUNearbyConversationInfo isEqualToConversationInfo:];
-[TUNearbyConversationInfo supportedHandoffTypes];
-[TUNearbyConversationInfo userProfileIdentifier];
```
