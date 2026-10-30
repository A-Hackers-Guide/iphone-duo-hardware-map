# `CUINamedIconLayerStack`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 1 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _layers;
```

## Properties

```
@property (T@"NSArray",&,N,V_layers) layers;
@property (T{CGSize=dd},R) size;
@property (T@"NSDictionary",R,N) renderingProperties;
@property (TS,R) sourceObjectVersion;
```

## Class methods

```
+[CUINamedIconLayerStack _createLayers:fromTheme:baseRendition:withBlock:];
```

## Instance methods

```
-[CUINamedIconLayerStack _removeLayerAtIndex:];
-[CUINamedIconLayerStack layers];
-[CUINamedIconLayerStack _addLayer:];
-[CUINamedIconLayerStack renderingProperties];
-[CUINamedIconLayerStack dataRepresentationWithError:];
-[CUINamedIconLayerStack dealloc];
-[CUINamedIconLayerStack size];
-[CUINamedIconLayerStack initWithName:usingRenditionKey:fromTheme:resolvingWithBlock:];
-[CUINamedIconLayerStack setLayers:];
-[CUINamedIconLayerStack mutableCopy];
-[CUINamedIconLayerStack _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedIconLayerStack _processIconGroups:layers:forName:andScale:layerIdentifier:error:];
-[CUINamedIconLayerStack _updateLayers:fromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedIconLayerStack iconLayerStackByAppendingLayerImages:];
-[CUINamedIconLayerStack iconLayerStackByAppendingLayers:];
-[CUINamedIconLayerStack sourceObjectVersion];
```
