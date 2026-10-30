# `AVURLAssetItemProviderData`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSSecurityScopedURLWrapper" _securityScopedURLWrapper;
@"NSDictionary" _assetInitializationOptions;
```

## Properties

```
@property (T@"NSURL",R,N) securityScopedURL;
@property (T@"NSDictionary",R,N,V_assetInitializationOptions) assetInitializationOptions;
```

## Class methods

```
+[AVURLAssetItemProviderData supportsSecureCoding];
+[AVURLAssetItemProviderData itemProviderDataWithURL:assetInitializationOptions:];
```

## Instance methods

```
-[AVURLAssetItemProviderData dealloc];
-[AVURLAssetItemProviderData encodeWithCoder:];
-[AVURLAssetItemProviderData initWithCoder:];
-[AVURLAssetItemProviderData securityScopedURL];
-[AVURLAssetItemProviderData assetInitializationOptions];
-[AVURLAssetItemProviderData initWithURL:assetInitializationOptions:];
```
