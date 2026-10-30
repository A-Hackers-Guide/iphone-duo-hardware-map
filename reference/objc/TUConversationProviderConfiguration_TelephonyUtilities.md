# `TUConversationProviderConfiguration`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 9 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _supportsLinks;
B _supportsSharePlay;
B _supportsConversationHandoff;
B _wantsLeaveOnInvalidation;
@"NSString" _serviceName;
@"NSString" _pseudonymFeatureID;
@"NSString" _bundleID;
@"NSSet" _supportedMediaTypes;
```

## Properties

```
@property (T@"NSString",C,N,V_serviceName) serviceName;
@property (TB,N,V_supportsLinks) supportsLinks;
@property (TB,N,V_supportsConversationHandoff) supportsConversationHandoff;
@property (TB,N,V_supportsSharePlay) supportsSharePlay;
@property (TB,R,N) supportsVideo;
@property (TB,N,V_wantsLeaveOnInvalidation) wantsLeaveOnInvalidation;
@property (T@"NSString",C,N,V_pseudonymFeatureID) pseudonymFeatureID;
@property (T@"NSString",C,N,V_bundleID) bundleID;
@property (T@"NSSet",C,N,V_supportedMediaTypes) supportedMediaTypes;
```

## Class methods

```
+[TUConversationProviderConfiguration supportsSecureCoding];
```

## Instance methods

```
-[TUConversationProviderConfiguration setSupportsLinks:];
-[TUConversationProviderConfiguration supportsLinks];
-[TUConversationProviderConfiguration isEqualToConversationProvider:];
-[TUConversationProviderConfiguration setBundleID:];
-[TUConversationProviderConfiguration initWithServiceName:];
-[TUConversationProviderConfiguration setWantsLeaveOnInvalidation:];
-[TUConversationProviderConfiguration initWithConfiguration:];
-[TUConversationProviderConfiguration setSupportsConversationHandoff:];
-[TUConversationProviderConfiguration serviceName];
-[TUConversationProviderConfiguration supportsConversationHandoff];
-[TUConversationProviderConfiguration setServiceName:];
-[TUConversationProviderConfiguration supportsVideo];
-[TUConversationProviderConfiguration encodeWithCoder:];
-[TUConversationProviderConfiguration pseudonymFeatureID];
-[TUConversationProviderConfiguration hash];
-[TUConversationProviderConfiguration description];
-[TUConversationProviderConfiguration initWithCoder:];
-[TUConversationProviderConfiguration bundleID];
-[TUConversationProviderConfiguration supportedMediaTypes];
-[TUConversationProviderConfiguration wantsLeaveOnInvalidation];
-[TUConversationProviderConfiguration copyWithZone:];
-[TUConversationProviderConfiguration isEqual:];
-[TUConversationProviderConfiguration setSupportedMediaTypes:];
-[TUConversationProviderConfiguration setSupportsSharePlay:];
-[TUConversationProviderConfiguration supportsSharePlay];
-[TUConversationProviderConfiguration setPseudonymFeatureID:];
```
