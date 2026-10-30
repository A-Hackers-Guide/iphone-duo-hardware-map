# `_UIIntelligenceLightSourceDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 1 properties, 8 instance methods, 9 class methods

## Instance variables

```
@? _builder;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Class methods

```
+[_UIIntelligenceLightSourceDescriptor shimmeringLight];
+[_UIIntelligenceLightSourceDescriptor _customDescriptorWithIdentifier:provider:];
+[_UIIntelligenceLightSourceDescriptor directionalLightWithConfiguration:];
+[_UIIntelligenceLightSourceDescriptor livingLightWithPalette:];
+[_UIIntelligenceLightSourceDescriptor livingLightWithPalette:seed:];
+[_UIIntelligenceLightSourceDescriptor sharedLight];
+[_UIIntelligenceLightSourceDescriptor sharedReactiveLight];
+[_UIIntelligenceLightSourceDescriptor sharedReactiveShimmeringLight];
+[_UIIntelligenceLightSourceDescriptor sharedShimmeringLight];
```

## Instance methods

```
-[_UIIntelligenceLightSourceDescriptor debugDescription];
-[_UIIntelligenceLightSourceDescriptor identifier];
-[_UIIntelligenceLightSourceDescriptor hash];
-[_UIIntelligenceLightSourceDescriptor copyWithZone:];
-[_UIIntelligenceLightSourceDescriptor isEqual:];
-[_UIIntelligenceLightSourceDescriptor _createLightSourceViewWithFrame:];
-[_UIIntelligenceLightSourceDescriptor descriptorWithModificationID:modifier:];
-[_UIIntelligenceLightSourceDescriptor initWithIdentifier:lightSourceViewProvider:];
```
