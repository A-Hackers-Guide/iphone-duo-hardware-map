# `MTLTextureBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- Protocols: `MTLTextureBinding`
- 3 instance variables, 14 properties, 6 instance methods, 0 class methods

## Instance variables

```
b15 _textureType;
b1 _isDepthTexture;
S _textureDataType;
```

## Properties

```
@property (TQ,R) textureType;
@property (TQ,R) textureDataType;
@property (TB,R,GisDepthTexture) depthTexture;
@property (TQ,R) arrayLength;
@property (T@"NSString",R) name;
@property (Tq,R) type;
@property (TQ,R) access;
@property (TQ,R) index;
@property (TB,R,GisUsed) used;
@property (TB,R,GisArgument) argument;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLTextureBindingInternal formattedDescription:];
-[MTLTextureBindingInternal textureType];
-[MTLTextureBindingInternal isDepthTexture];
-[MTLTextureBindingInternal textureDataType];
-[MTLTextureBindingInternal isEqual:];
-[MTLTextureBindingInternal initWithName:access:isActive:locationIndex:arraySize:dataType:textureType:isDepthTexture:];
```
