# `CUINamedImageAtlas`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 3 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _images;
@"NSArray" _renditions;
^{__CFArray=} _atlasImages;
```

## Properties

```
@property (T^{CGImage=},R,N) image;
@property (T^{__CFArray=},R,N) images;
@property (Td,R,N) scale;
@property (T@"NSArray",R,N) imageNames;
@property (TB,R,N) completeTextureExtrusion;
```

## Instance methods

```
-[CUINamedImageAtlas dealloc];
-[CUINamedImageAtlas images];
-[CUINamedImageAtlas scale];
-[CUINamedImageAtlas image];
-[CUINamedImageAtlas imageWithName:];
-[CUINamedImageAtlas completeTextureExtrusion];
-[CUINamedImageAtlas imageNames];
-[CUINamedImageAtlas initWithName:usingRenditionKey:withContents:contentsFromCatalog:fromTheme:withSourceThemeRef:];
```
