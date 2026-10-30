# `EspressoContext`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<Espresso::abstract_context>="__ptr_"^{abstract_context}"__cntrl_"^{__shared_weak_count}} _ctx;
```

## Properties

```
@property (T{shared_ptr<Espresso::abstract_context>=^{abstract_context}^{__shared_weak_count}},R,V_ctx) ctx;
@property (Ti,R) platform;
```

## Instance methods

```
-[EspressoContext initWithContext:];
-[EspressoContext initWithPlatform:];
-[EspressoContext platform];
-[EspressoContext ctx];
-[EspressoContext initWithDevice:andWisdomParams:];
-[EspressoContext initWithNetworkContext:];
-[EspressoContext set_priority:low_priority_max_ms_per_command_buffer:gpu_priority:];
```
