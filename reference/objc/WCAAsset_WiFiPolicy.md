# `WCAAsset`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 4 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _extension;
Q _latestInstalledVersion;
@"MAAsset" _latestInstalledAsset;
Q _installedAssetVersion;
Q _latestNotInstalledVersion;
@"MAAsset" _latestNotInstalledAsset;
```

## Properties

```
@property (TQ,V_latestInstalledVersion) latestInstalledVersion;
@property (T@"MAAsset",&,N,V_latestInstalledAsset) latestInstalledAsset;
@property (TQ,V_installedAssetVersion) installedAssetVersion;
@property (TQ,V_latestNotInstalledVersion) latestNotInstalledVersion;
@property (T@"MAAsset",&,N,V_latestNotInstalledAsset) latestNotInstalledAsset;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_extension) extension;
```

## Class methods

```
+[WCAAsset supportsSecureCoding];
+[WCAAsset assetWithName:andExtension:];
+[WCAAsset beaconsDataAsset];
+[WCAAsset wifiBehaviorPlistAsset];
```

## Instance methods

```
-[WCAAsset latestInstalledVersion];
-[WCAAsset latestInstalledAsset];
-[WCAAsset setLatestInstalledAsset:];
-[WCAAsset setLatestNotInstalledVersion:];
-[WCAAsset setLatestInstalledVersion:];
-[WCAAsset encodeWithCoder:];
-[WCAAsset setLatestNotInstalledAsset:];
-[WCAAsset latestNotInstalledVersion];
-[WCAAsset installedAssetVersion];
-[WCAAsset description];
-[WCAAsset setName:];
-[WCAAsset initWithCoder:];
-[WCAAsset extension];
-[WCAAsset isEqual:];
-[WCAAsset name];
-[WCAAsset setExtension:];
-[WCAAsset setInstalledAssetVersion:];
-[WCAAsset latestNotInstalledAsset];
```
