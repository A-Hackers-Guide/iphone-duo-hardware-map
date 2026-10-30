# `_UICoreUICatalogColorWrapper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 6 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _nibLoadingBundleID;
@"NSMutableDictionary" _colorCache;
B _hasLoggedFailure;
@"NSString" _name;
@"NSString" _bundleID;
@"UIColor" _fallbackColor;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_bundleID) bundleID;
@property (T@"UIColor",R,N,V_fallbackColor) fallbackColor;
@property (T@"UIColor",R,N) color;
```

## Instance methods

```
-[_UICoreUICatalogColorWrapper bundle];
-[_UICoreUICatalogColorWrapper color];
-[_UICoreUICatalogColorWrapper encodeWithCoder:];
-[_UICoreUICatalogColorWrapper hash];
-[_UICoreUICatalogColorWrapper description];
-[_UICoreUICatalogColorWrapper initWithCoder:];
-[_UICoreUICatalogColorWrapper bundleID];
-[_UICoreUICatalogColorWrapper copyWithZone:];
-[_UICoreUICatalogColorWrapper isEqual:];
-[_UICoreUICatalogColorWrapper name];
-[_UICoreUICatalogColorWrapper _uikit_valueForTraitCollection:];
-[_UICoreUICatalogColorWrapper _uikit_variesByTraitCollections];
-[_UICoreUICatalogColorWrapper setCachedColor:forDisplayGamut:];
-[_UICoreUICatalogColorWrapper cachedColorForDisplayGamut:];
-[_UICoreUICatalogColorWrapper cgColorForTraitCollection:];
-[_UICoreUICatalogColorWrapper colorCache];
-[_UICoreUICatalogColorWrapper fallbackColor];
-[_UICoreUICatalogColorWrapper initWithName:bundleID:fallbackColor:];
-[_UICoreUICatalogColorWrapper isEqualToCoreUICatalogColor:];
-[_UICoreUICatalogColorWrapper nibLoadingBundle];
```
