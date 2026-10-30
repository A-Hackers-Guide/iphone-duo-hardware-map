# `DSSourceRepository`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _sourcesByName;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_sourcesByName) sourcesByName;
@property (T@"NSArray",R,C,N) sources;
```

## Class methods

```
+[DSSourceRepository initialize];
+[DSSourceRepository repositoryWithURL:];
+[DSSourceRepository runtimeFeatureFlagsEnabledFor:];
```

## Instance methods

```
-[DSSourceRepository init];
-[DSSourceRepository objectForKeyedSubscript:];
-[DSSourceRepository sources];
-[DSSourceRepository initWithSources:];
-[DSSourceRepository defaultDir];
-[DSSourceRepository setSourcesByName:];
-[DSSourceRepository sourcesByName];
```
