# `CUINamedSolidLayerStack`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- Protocols: `CUINamedLayerStackProtocol`
- 2 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _layers;
@"CUIThemeRendition" _flattenedImageRendition;
```

## Properties

```
@property (T@"NSArray",&,N,V_layers) layers;
@property (T{CGSize=dd},R,N) size;
@property (T^{CGImage=},R,N) flattenedImage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CUINamedSolidLayerStack layers];
-[CUINamedSolidLayerStack dealloc];
-[CUINamedSolidLayerStack size];
-[CUINamedSolidLayerStack initWithName:usingRenditionKey:fromTheme:resolvingWithBlock:];
-[CUINamedSolidLayerStack hash];
-[CUINamedSolidLayerStack setLayers:];
-[CUINamedSolidLayerStack isEqual:];
-[CUINamedSolidLayerStack flattenedImage];
-[CUINamedSolidLayerStack layerImageAtIndex:];
```
