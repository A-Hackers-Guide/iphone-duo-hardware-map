# `CUINamedSolidLayerImage`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedImage`
- Protocols: `CUINamedLayerImageProtocol`
- 8 instance variables, 10 properties, 12 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
d _opacity;
i _blendMode;
@"CUINamedTexture" _edgeTexture;
@"CUINamedTexture" _gradientTexture;
@"TXRTexture" _edgeTXR;
@"TXRTexture" _gradientTXR;
B _fixedFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (Td,N,V_opacity) opacity;
@property (Ti,N,V_blendMode) blendMode;
@property (TB,N,V_fixedFrame) fixedFrame;
@property (T^{CGImage=},R,N) image;
@property (Td,R,N) scale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CUINamedSolidLayerImage dealloc];
-[CUINamedSolidLayerImage opacity];
-[CUINamedSolidLayerImage initWithName:usingRenditionKey:fromTheme:];
-[CUINamedSolidLayerImage setOpacity:];
-[CUINamedSolidLayerImage setFrame:];
-[CUINamedSolidLayerImage setFixedFrame:];
-[CUINamedSolidLayerImage blendMode];
-[CUINamedSolidLayerImage fixedFrame];
-[CUINamedSolidLayerImage setBlendMode:];
-[CUINamedSolidLayerImage frame];
-[CUINamedSolidLayerImage edgeDefinitionTextureWithBufferAllocator:];
-[CUINamedSolidLayerImage gradientTextureWithBufferAllocator:];
```
