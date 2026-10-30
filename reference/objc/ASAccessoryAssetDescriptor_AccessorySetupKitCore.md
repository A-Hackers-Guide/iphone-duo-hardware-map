# `ASAccessoryAssetDescriptor`

- Image: [`/System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore`](../userland/System__Library__PrivateFrameworks__AccessorySetupKitCore.framework__AccessorySetupKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 11 instance variables, 13 properties, 23 instance methods, 4 class methods

## Instance variables

```
q kind;
? data;
? contentType;
? name;
? bundleIdentifier;
? url;
B isTemplate;
d pixelWidth;
d pixelHeight;
d scale;
? imageAccessibilityLabel;
```

## Properties

```
@property (Tq,N,R,Vkind) kind;
@property (T@"NSData",N,R) data;
@property (T@"NSString",N,R) contentType;
@property (T@"NSString",N,R) name;
@property (T@"NSString",N,R) bundleIdentifier;
@property (T@"NSURL",N,R) url;
@property (TB,N,R,VisTemplate) isTemplate;
@property (Td,N,R,VpixelWidth) pixelWidth;
@property (Td,N,R,VpixelHeight) pixelHeight;
@property (Td,N,R,Vscale) scale;
@property (TB,N,R) hasPixelDimensions;
@property (T@"NSString",N,R) imageAccessibilityLabel;
@property (Tq,N,R) hash;
```

## Class methods

```
+[ASAccessoryAssetDescriptor supportsSecureCoding];
+[ASAccessoryAssetDescriptor arrayFromData:];
+[ASAccessoryAssetDescriptor arrayToData:];
+[ASAccessoryAssetDescriptor fromData:];
```

## Instance methods

```
-[ASAccessoryAssetDescriptor pixelWidth];
-[ASAccessoryAssetDescriptor init];
-[ASAccessoryAssetDescriptor pixelHeight];
-[ASAccessoryAssetDescriptor contentType];
-[ASAccessoryAssetDescriptor data];
-[ASAccessoryAssetDescriptor bundleIdentifier];
-[ASAccessoryAssetDescriptor scale];
-[ASAccessoryAssetDescriptor encodeWithCoder:];
-[ASAccessoryAssetDescriptor hash];
-[ASAccessoryAssetDescriptor initWithCoder:];
-[ASAccessoryAssetDescriptor copyWithZone:];
-[ASAccessoryAssetDescriptor isEqual:];
-[ASAccessoryAssetDescriptor name];
-[ASAccessoryAssetDescriptor kind];
-[ASAccessoryAssetDescriptor url];
-[ASAccessoryAssetDescriptor isTemplate];
-[ASAccessoryAssetDescriptor toData];
-[ASAccessoryAssetDescriptor hasPixelDimensions];
-[ASAccessoryAssetDescriptor imageAccessibilityLabel];
-[ASAccessoryAssetDescriptor initWithAssetName:bundleIdentifier:scale:isTemplate:imageAccessibilityLabel:];
-[ASAccessoryAssetDescriptor initWithData:contentType:scale:pixelWidth:pixelHeight:isTemplate:imageAccessibilityLabel:];
-[ASAccessoryAssetDescriptor initWithSymbolName:isTemplate:imageAccessibilityLabel:];
-[ASAccessoryAssetDescriptor initWithURL:contentType:scale:isTemplate:imageAccessibilityLabel:];
```
