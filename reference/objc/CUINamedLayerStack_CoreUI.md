# `CUINamedLayerStack`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- Protocols: `CUINamedLayerStackProtocol`
- 3 instance variables, 8 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _layers;
@"CUIThemeRendition" _flattenedImageRendition;
@"CUIThemeRendition" _radiosityImageRendition;
```

## Properties

```
@property (T@"NSArray",&,N,V_layers) layers;
@property (T^{CGImage=},R,N) radiosityImage;
@property (T{CGSize=dd},R,N) size;
@property (T^{CGImage=},R,N) flattenedImage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CUINamedLayerStack radiosityImageWithImage:displayScale:completionHandler:];
+[CUINamedLayerStack _doRadiosityBlurOnPixelBuffer:bytesPerRow:bitsPerPixel:width:height:scaleFactor:usesGaussianBlur:adjustedSize:];
+[CUINamedLayerStack createRadiosityImageWithImage:displayScale:];
```

## Instance methods

```
-[CUINamedLayerStack layers];
-[CUINamedLayerStack dealloc];
-[CUINamedLayerStack size];
-[CUINamedLayerStack initWithName:usingRenditionKey:fromTheme:resolvingWithBlock:];
-[CUINamedLayerStack hash];
-[CUINamedLayerStack setLayers:];
-[CUINamedLayerStack isEqual:];
-[CUINamedLayerStack flattenedImage];
-[CUINamedLayerStack radiosityImage];
-[CUINamedLayerStack layerImageAtIndex:];
```
