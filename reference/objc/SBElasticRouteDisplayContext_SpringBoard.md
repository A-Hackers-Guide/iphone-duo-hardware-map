# `SBElasticRouteDisplayContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBElasticRouteDisplaying`
- 4 instance variables, 8 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _localizedDisplayName;
@? _glyphStateValueTransformer;
@"CCUICAPackageDescription" _glyphPackage;
@"UIImage" _glyphImage;
```

## Properties

```
@property (T@"NSString",&,N,V_localizedDisplayName) localizedDisplayName;
@property (T@?,C,N,V_glyphStateValueTransformer) glyphStateValueTransformer;
@property (T@"CCUICAPackageDescription",&,N,V_glyphPackage) glyphPackage;
@property (T@"UIImage",&,N,V_glyphImage) glyphImage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBElasticRouteDisplayContext routeContextWithName:glyphImage:];
+[SBElasticRouteDisplayContext routeContextWithName:valueTransformer:glyphPackage:];
```

## Instance methods

```
-[SBElasticRouteDisplayContext localizedDisplayName];
-[SBElasticRouteDisplayContext description];
-[SBElasticRouteDisplayContext setGlyphImage:];
-[SBElasticRouteDisplayContext setLocalizedDisplayName:];
-[SBElasticRouteDisplayContext glyphImage];
-[SBElasticRouteDisplayContext _initWithName:glyphStateValueTransformer:glyphPackage:glyphImage:];
-[SBElasticRouteDisplayContext glyphPackage];
-[SBElasticRouteDisplayContext glyphStateValueTransformer];
-[SBElasticRouteDisplayContext setGlyphPackage:];
-[SBElasticRouteDisplayContext setGlyphStateValueTransformer:];
```
