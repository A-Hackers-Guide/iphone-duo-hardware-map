# `ASPickerDisplayItem`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 25 instance methods, 4 class methods

## Instance variables

```
B _allowsRename;
@"NSString" _name;
@"UIImage" _productImage;
@"ASDiscoveryDescriptor" _descriptor;
Q _renameOptions;
Q _setupOptions;
@"UTType" _accessoryType;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"UIImage",C,N,V_productImage) productImage;
@property (T@"UTType",R,C,N,V_accessoryType) accessoryType;
@property (TB,N,V_allowsRename) allowsRename;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"ASDiscoveryDescriptor",R,C,N,V_descriptor) descriptor;
@property (TQ,N,V_renameOptions) renameOptions;
@property (TQ,N,V_setupOptions) setupOptions;
```

## Class methods

```
+[ASPickerDisplayItem supportsSecureCoding];
+[ASPickerDisplayItem arrayFromData:];
+[ASPickerDisplayItem arrayToData:];
+[ASPickerDisplayItem fromData:];
```

## Instance methods

```
-[ASPickerDisplayItem encodeWithXPCObject:];
-[ASPickerDisplayItem initWithXPCObject:error:];
-[ASPickerDisplayItem descriptor];
-[ASPickerDisplayItem descriptionWithLevel:];
-[ASPickerDisplayItem identifier];
-[ASPickerDisplayItem encodeWithCoder:];
-[ASPickerDisplayItem description];
-[ASPickerDisplayItem setName:];
-[ASPickerDisplayItem initWithCoder:];
-[ASPickerDisplayItem copyWithZone:];
-[ASPickerDisplayItem isEqual:];
-[ASPickerDisplayItem name];
-[ASPickerDisplayItem accessoryType];
-[ASPickerDisplayItem resizedImage];
-[ASPickerDisplayItem allowsRename];
-[ASPickerDisplayItem discoveryConfigurationWithBundleID:];
-[ASPickerDisplayItem initWithName:productImage:descriptor:];
-[ASPickerDisplayItem productImage];
-[ASPickerDisplayItem renameOptions];
-[ASPickerDisplayItem setAllowsRename:];
-[ASPickerDisplayItem setProductImage:];
-[ASPickerDisplayItem setRenameOptions:];
-[ASPickerDisplayItem setSetupOptions:];
-[ASPickerDisplayItem setupOptions];
-[ASPickerDisplayItem toData];
```
