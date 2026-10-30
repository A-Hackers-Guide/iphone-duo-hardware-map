# `CTLazuliSystemConfiguration`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 18 instance variables, 18 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _featureSupported;
B _featureEnabledByDefault;
B _featureDisabledByProfile;
B _featureDisabledStoreDemo;
B _bsfUsesSecureTransport;
B _supportsSecurity;
@"CTLazuliMessagingCapabilities" _messagingCapabilities;
@"CTLazuliChatCapabilities" _chatCapabilities;
@"CTLazuliGroupChatCapabilities" _groupChatCapabilites;
@"CTLazuliFileTransferCapabilities" _fileTransferCapabilities;
@"CTLazuliOperationStatus" _operationStatus;
@"CTLazuliDiscoveryCapabilities" _discoverCapabilities;
@"CTLazuliUserIdentities" _identity;
@"CTLazuliBusinessMessagingCapabilities" _businessMessagingCapabilities;
@"CTLazuliEncryptionCapabilities" _encryptionCapabilities;
@"CTLazuliStaticFeatureProperties" _staticFeatureProperties;
@"NSNumber" _bsfPort;
@"NSString" _networkAttributionBundleID;
```

## Properties

```
@property (T@"CTLazuliMessagingCapabilities",&,N,V_messagingCapabilities) messagingCapabilities;
@property (T@"CTLazuliChatCapabilities",&,N,V_chatCapabilities) chatCapabilities;
@property (T@"CTLazuliGroupChatCapabilities",&,N,V_groupChatCapabilites) groupChatCapabilites;
@property (T@"CTLazuliFileTransferCapabilities",&,N,V_fileTransferCapabilities) fileTransferCapabilities;
@property (T@"CTLazuliOperationStatus",&,N,V_operationStatus) operationStatus;
@property (T@"CTLazuliDiscoveryCapabilities",&,N,V_discoverCapabilities) discoverCapabilities;
@property (T@"CTLazuliUserIdentities",&,N,V_identity) identity;
@property (T@"CTLazuliBusinessMessagingCapabilities",&,N,V_businessMessagingCapabilities) businessMessagingCapabilities;
@property (T@"CTLazuliEncryptionCapabilities",&,N,V_encryptionCapabilities) encryptionCapabilities;
@property (T@"CTLazuliStaticFeatureProperties",&,N,V_staticFeatureProperties) staticFeatureProperties;
@property (TB,N,V_featureSupported) featureSupported;
@property (TB,N,V_featureEnabledByDefault) featureEnabledByDefault;
@property (TB,N,V_featureDisabledByProfile) featureDisabledByProfile;
@property (TB,N,V_featureDisabledStoreDemo) featureDisabledStoreDemo;
@property (T@"NSNumber",&,N,V_bsfPort) bsfPort;
@property (TB,N,V_bsfUsesSecureTransport) bsfUsesSecureTransport;
@property (TB,N,V_supportsSecurity) supportsSecurity;
@property (T@"NSString",&,N,V_networkAttributionBundleID) networkAttributionBundleID;
```

## Class methods

```
+[CTLazuliSystemConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliSystemConfiguration setIdentity:];
-[CTLazuliSystemConfiguration encodeWithCoder:];
-[CTLazuliSystemConfiguration identity];
-[CTLazuliSystemConfiguration description];
-[CTLazuliSystemConfiguration initWithCoder:];
-[CTLazuliSystemConfiguration copyWithZone:];
-[CTLazuliSystemConfiguration isEqual:];
-[CTLazuliSystemConfiguration bsfPort];
-[CTLazuliSystemConfiguration operationStatus];
-[CTLazuliSystemConfiguration bsfUsesSecureTransport];
-[CTLazuliSystemConfiguration businessMessagingCapabilities];
-[CTLazuliSystemConfiguration chatCapabilities];
-[CTLazuliSystemConfiguration discoverCapabilities];
-[CTLazuliSystemConfiguration encryptionCapabilities];
-[CTLazuliSystemConfiguration featureDisabledByProfile];
-[CTLazuliSystemConfiguration featureDisabledStoreDemo];
-[CTLazuliSystemConfiguration featureEnabledByDefault];
-[CTLazuliSystemConfiguration featureSupported];
-[CTLazuliSystemConfiguration fileTransferCapabilities];
-[CTLazuliSystemConfiguration groupChatCapabilites];
-[CTLazuliSystemConfiguration initWithReflection:];
-[CTLazuliSystemConfiguration isEqualToCTLazuliSystemConfiguration:];
-[CTLazuliSystemConfiguration messagingCapabilities];
-[CTLazuliSystemConfiguration networkAttributionBundleID];
-[CTLazuliSystemConfiguration setBsfPort:];
-[CTLazuliSystemConfiguration setBsfUsesSecureTransport:];
-[CTLazuliSystemConfiguration setBusinessMessagingCapabilities:];
-[CTLazuliSystemConfiguration setChatCapabilities:];
-[CTLazuliSystemConfiguration setDiscoverCapabilities:];
-[CTLazuliSystemConfiguration setEncryptionCapabilities:];
-[CTLazuliSystemConfiguration setFeatureDisabledByProfile:];
-[CTLazuliSystemConfiguration setFeatureDisabledStoreDemo:];
-[CTLazuliSystemConfiguration setFeatureEnabledByDefault:];
-[CTLazuliSystemConfiguration setFeatureSupported:];
-[CTLazuliSystemConfiguration setFileTransferCapabilities:];
-[CTLazuliSystemConfiguration setGroupChatCapabilites:];
-[CTLazuliSystemConfiguration setMessagingCapabilities:];
-[CTLazuliSystemConfiguration setNetworkAttributionBundleID:];
-[CTLazuliSystemConfiguration setOperationStatus:];
-[CTLazuliSystemConfiguration setStaticFeatureProperties:];
-[CTLazuliSystemConfiguration setSupportsSecurity:];
-[CTLazuliSystemConfiguration staticFeatureProperties];
-[CTLazuliSystemConfiguration supportsSecurity];
```
