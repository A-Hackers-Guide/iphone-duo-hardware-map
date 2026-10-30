# `ETImagePreprocessParams`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _network_wants_bgr;
f _bias_r;
f _bias_g;
f _bias_b;
f _scale;
Q _channels;
Q _height;
Q _width;
```

## Properties

```
@property (TB,R,N,V_network_wants_bgr) network_wants_bgr;
@property (Tf,R,N,V_bias_r) bias_r;
@property (Tf,R,N,V_bias_g) bias_g;
@property (Tf,R,N,V_bias_b) bias_b;
@property (Tf,R,N,V_scale) scale;
@property (TQ,R,N,V_channels) channels;
@property (TQ,R,N,V_height) height;
@property (TQ,R,N,V_width) width;
```

## Instance methods

```
-[ETImagePreprocessParams channels];
-[ETImagePreprocessParams scale];
-[ETImagePreprocessParams width];
-[ETImagePreprocessParams height];
-[ETImagePreprocessParams bias_b];
-[ETImagePreprocessParams bias_g];
-[ETImagePreprocessParams bias_r];
-[ETImagePreprocessParams initWithHeight:Width:NumChannels:Scale:BiasR:BiasG:BiasB:NetworkWantBGR:];
-[ETImagePreprocessParams network_wants_bgr];
```
