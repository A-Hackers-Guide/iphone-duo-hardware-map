# `PKStrokeRenderState`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
d _particleOffset;
d _secondaryParticleOffset;
{CGPoint="x"d"y"d} _grainOffset;
```

## Properties

```
@property (T{CGPoint=dd},N,V_grainOffset) grainOffset;
```

## Class methods

```
+[PKStrokeRenderState supportsSecureCoding];
```

## Instance methods

```
-[PKStrokeRenderState _isDefault];
-[PKStrokeRenderState init];
-[PKStrokeRenderState _particleOffset];
-[PKStrokeRenderState initWithArchive:];
-[PKStrokeRenderState encodeWithCoder:];
-[PKStrokeRenderState hash];
-[PKStrokeRenderState saveToArchive:];
-[PKStrokeRenderState initWithCoder:];
-[PKStrokeRenderState _secondaryParticleOffset];
-[PKStrokeRenderState copyWithZone:];
-[PKStrokeRenderState isEqual:];
-[PKStrokeRenderState setGrainOffset:];
-[PKStrokeRenderState _setParticleOffset:];
-[PKStrokeRenderState _setSecondaryParticleOffset:];
-[PKStrokeRenderState grainOffset];
```
