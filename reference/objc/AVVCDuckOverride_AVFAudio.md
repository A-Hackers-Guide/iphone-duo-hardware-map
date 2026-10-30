# `AVVCDuckOverride`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isBlur;
@"NSNumber" _duckOthers;
@"NSNumber" _duckToLevel;
@"NSNumber" _mixWithOthers;
```

## Properties

```
@property (T@"NSNumber",&,N,V_duckOthers) duckOthers;
@property (T@"NSNumber",&,N,V_duckToLevel) duckToLevel;
@property (TB,N,V_isBlur) isBlur;
@property (T@"NSNumber",&,N,V_mixWithOthers) mixWithOthers;
```

## Instance methods

```
-[AVVCDuckOverride init];
-[AVVCDuckOverride description];
-[AVVCDuckOverride duckOthers];
-[AVVCDuckOverride setDuckOthers:];
-[AVVCDuckOverride setDuckToLevel:];
-[AVVCDuckOverride duckToLevel];
-[AVVCDuckOverride initWithDuckOthers:duckToLevel:mixWithOthers:];
-[AVVCDuckOverride isBlur];
-[AVVCDuckOverride mixWithOthers];
-[AVVCDuckOverride setIsBlur:];
-[AVVCDuckOverride setMixWithOthers:];
```
