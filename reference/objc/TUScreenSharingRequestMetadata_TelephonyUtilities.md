# `TUScreenSharingRequestMetadata`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"NSString" _appName;
@"NSString" _sceneID;
```

## Properties

```
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",&,N,V_appName) appName;
@property (T@"NSString",&,N,V_sceneID) sceneID;
```

## Class methods

```
+[TUScreenSharingRequestMetadata supportsSecureCoding];
```

## Instance methods

```
-[TUScreenSharingRequestMetadata sceneID];
-[TUScreenSharingRequestMetadata appName];
-[TUScreenSharingRequestMetadata setSceneID:];
-[TUScreenSharingRequestMetadata bundleIdentifier];
-[TUScreenSharingRequestMetadata setAppName:];
-[TUScreenSharingRequestMetadata encodeWithCoder:];
-[TUScreenSharingRequestMetadata hash];
-[TUScreenSharingRequestMetadata description];
-[TUScreenSharingRequestMetadata initWithCoder:];
-[TUScreenSharingRequestMetadata setBundleIdentifier:];
-[TUScreenSharingRequestMetadata copyWithZone:];
-[TUScreenSharingRequestMetadata isEqual:];
-[TUScreenSharingRequestMetadata isEqualToScreenSharingRequestMetadata:];
```
