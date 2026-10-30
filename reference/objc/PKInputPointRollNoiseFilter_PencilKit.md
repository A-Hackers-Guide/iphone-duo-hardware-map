# `PKInputPointRollNoiseFilter`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKInputPointBaseFilter`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{linear_congruential_engine<unsigned int, 48271U, 0U, 2147483647U>="__x_"I} generator;
d currentRollOffsetValue;
d _rollJitterNoise;
d _rollOffsetNoise;
```

## Instance methods

```
-[PKInputPointRollNoiseFilter resetFilter];
-[PKInputPointRollNoiseFilter _recalculateOffset];
-[PKInputPointRollNoiseFilter addInputPoint:];
```
