# `UICornerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `NSCoding`
- 1 instance variables, 2 properties, 7 instance methods, 14 class methods

## Instance variables

```
impl;
```

## Properties

```
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UICornerConfiguration supportsSecureCoding];
+[UICornerConfiguration configurationWithUniformLeftRadius:topRightRadius:bottomRightRadius:];
+[UICornerConfiguration configurationWithUniformTopRadius:uniformBottomRadius:];
+[UICornerConfiguration configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:];
+[UICornerConfiguration capsuleConfiguration];
+[UICornerConfiguration configurationWithUniformTopRadius:bottomLeftRadius:bottomRightRadius:];
+[UICornerConfiguration capsuleConfigurationWithMaximumRadius:];
+[UICornerConfiguration configurationWithUniformRadius:];
+[UICornerConfiguration unspecifiedConfiguration];
+[UICornerConfiguration configurationWithRadius:];
+[UICornerConfiguration configurationWithUniformRightRadius:topLeftRadius:bottomLeftRadius:];
+[UICornerConfiguration configurationWithUniformBottomRadius:topLeftRadius:topRightRadius:];
+[UICornerConfiguration configurationWithUniformLeftRadius:uniformRightRadius:];
+[UICornerConfiguration _configurationWithRadius:mask:];
```

## Instance methods

```
-[UICornerConfiguration init];
-[UICornerConfiguration encodeWithCoder:];
-[UICornerConfiguration hash];
-[UICornerConfiguration description];
-[UICornerConfiguration initWithCoder:];
-[UICornerConfiguration copyWithZone:];
-[UICornerConfiguration isEqual:];
```
