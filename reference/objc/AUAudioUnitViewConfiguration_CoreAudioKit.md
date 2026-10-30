# `AUAudioUnitViewConfiguration`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _hostHasController;
d _width;
d _height;
```

## Properties

```
@property (Td,R,N,V_width) width;
@property (Td,R,N,V_height) height;
@property (TB,R,N,V_hostHasController) hostHasController;
```

## Class methods

```
+[AUAudioUnitViewConfiguration supportsSecureCoding];
```

## Instance methods

```
-[AUAudioUnitViewConfiguration encodeWithCoder:];
-[AUAudioUnitViewConfiguration hash];
-[AUAudioUnitViewConfiguration initWithCoder:];
-[AUAudioUnitViewConfiguration width];
-[AUAudioUnitViewConfiguration isEqual:];
-[AUAudioUnitViewConfiguration height];
-[AUAudioUnitViewConfiguration hostHasController];
-[AUAudioUnitViewConfiguration initWithWidth:height:hostHasController:];
```
