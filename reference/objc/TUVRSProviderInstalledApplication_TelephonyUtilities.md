# `TUVRSProviderInstalledApplication`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _supportsLiveCommunication;
@"NSString" _bundleIdentifier;
@"NSString" _localizedName;
@"NSData" _iconImageData;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_localizedName) localizedName;
@property (TB,R,N,V_supportsLiveCommunication) supportsLiveCommunication;
@property (T@"NSData",R,C,N,V_iconImageData) iconImageData;
```

## Class methods

```
+[TUVRSProviderInstalledApplication supportsSecureCoding];
```

## Instance methods

```
-[TUVRSProviderInstalledApplication bundleIdentifier];
-[TUVRSProviderInstalledApplication localizedName];
-[TUVRSProviderInstalledApplication encodeWithCoder:];
-[TUVRSProviderInstalledApplication hash];
-[TUVRSProviderInstalledApplication description];
-[TUVRSProviderInstalledApplication initWithCoder:];
-[TUVRSProviderInstalledApplication copyWithZone:];
-[TUVRSProviderInstalledApplication isEqual:];
-[TUVRSProviderInstalledApplication iconImageData];
-[TUVRSProviderInstalledApplication initWithBundleIdentifier:localizedName:supportsLiveCommunication:iconImageData:];
-[TUVRSProviderInstalledApplication isEqualToInstalledApplication:];
-[TUVRSProviderInstalledApplication supportsLiveCommunication];
```
