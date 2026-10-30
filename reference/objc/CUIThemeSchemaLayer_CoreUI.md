# `CUIThemeSchemaLayer`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _renditions;
@"NSString" _name;
Q _index;
```

## Properties

```
@property (T@"NSArray",&,N,V_renditions) renditions;
@property (T@"NSString",&,N,V_name) name;
@property (TQ,N,V_index) index;
```

## Class methods

```
+[CUIThemeSchemaLayer layerWithRenditions:name:index:];
```

## Instance methods

```
-[CUIThemeSchemaLayer dealloc];
-[CUIThemeSchemaLayer index];
-[CUIThemeSchemaLayer setIndex:];
-[CUIThemeSchemaLayer description];
-[CUIThemeSchemaLayer setName:];
-[CUIThemeSchemaLayer name];
-[CUIThemeSchemaLayer calculateColumLefts:rowTops:totalSize:forPartFeatures:];
-[CUIThemeSchemaLayer initWithRenditions:name:index:];
-[CUIThemeSchemaLayer renditions];
-[CUIThemeSchemaLayer setRenditions:];
-[CUIThemeSchemaLayer translateFromWidthsOrHeightsToLeftsOrTops:leftsOrTops:];
```
