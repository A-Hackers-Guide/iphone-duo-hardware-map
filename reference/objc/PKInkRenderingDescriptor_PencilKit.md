# `PKInkRenderingDescriptor`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _type;
Q _blendMode;
Q _alternateMode;
@"PKInkParticleDescriptor" _particleDescriptor;
@"PKInkParticleDescriptor" _secondaryParticleDescriptor;
```

## Properties

```
@property (TQ,R,N,V_type) type;
@property (TQ,R,N,V_alternateMode) alternateMode;
@property (TQ,R,N,V_blendMode) blendMode;
@property (T@"PKInkParticleDescriptor",R,N,V_particleDescriptor) particleDescriptor;
@property (T@"PKInkParticleDescriptor",R,N,V_secondaryParticleDescriptor) secondaryParticleDescriptor;
```

## Instance methods

```
-[PKInkRenderingDescriptor type];
-[PKInkRenderingDescriptor blendMode];
-[PKInkRenderingDescriptor mutableCopy];
-[PKInkRenderingDescriptor alternateMode];
-[PKInkRenderingDescriptor initWithType:blendMode:alternateMode:particleDescriptor:secondaryParticleDescriptor:];
-[PKInkRenderingDescriptor particleDescriptor];
-[PKInkRenderingDescriptor secondaryParticleDescriptor];
```
