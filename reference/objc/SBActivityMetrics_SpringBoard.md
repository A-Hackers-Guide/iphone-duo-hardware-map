# `SBActivityMetrics`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSActivityMetricsProviding`
- 4 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIWindowScene" _windowScene;
@"ACUISActivityHostViewControllerConfiguration" _configuration;
@"<CSActivityMetricsContextProviding>" _metricsContext;
Q _activeLayoutDirection;
```

## Properties

```
@property (T@"UIWindowScene",&,N,V_windowScene) windowScene;
@property (T@"ACUISActivityHostViewControllerConfiguration",R,N,V_configuration) configuration;
@property (TQ,R,N,V_activeLayoutDirection) activeLayoutDirection;
@property (T@"UIWindowScene",R,N) metricsWindowScene;
@property (T@"<CSActivityMetricsContextProviding>",?,W,N,V_metricsContext) metricsContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityMetrics setWindowScene:];
-[SBActivityMetrics modalFullScreenMetrics];
-[SBActivityMetrics metricsRequestForConfiguration:];
-[SBActivityMetrics init];
-[SBActivityMetrics initWithConfiguration:windowScene:activeLayoutDirection:];
-[SBActivityMetrics _metricsForWindowScene:];
-[SBActivityMetrics metricsContext];
-[SBActivityMetrics initialMetricsRequest];
-[SBActivityMetrics defaultMetrics];
-[SBActivityMetrics configuration];
-[SBActivityMetrics activeLayoutDirection];
-[SBActivityMetrics metricsRequestForWindowScene:];
-[SBActivityMetrics ambientWidgetMetrics];
-[SBActivityMetrics setMetricsContext:];
-[SBActivityMetrics metricsWindowScene];
-[SBActivityMetrics _isHostingAmbientAlertSceneForConfiguration:];
-[SBActivityMetrics initWithConfiguration:windowScene:];
-[SBActivityMetrics windowScene];
-[SBActivityMetrics ambientDefaultMetricsForContentType:];
-[SBActivityMetrics ambientCompactDefaultMetrics];
```
