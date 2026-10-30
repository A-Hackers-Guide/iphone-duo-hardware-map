# `PolyNomialExtrapolation`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
i _N;
i _n;
[2{Matrix<float, 0U, 0U, false>="m_data"^f"m_capacity"Q"m_rows"I"m_cols"I}] _A;
[2{Matrix<float, 0U, 1U, false>="m_data"^f"m_capacity"Q"m_rows"I}] _b;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _g;
{deque<float, std::allocator<float>>="__map_"{__split_buffer<float *, std::allocator<float *>>="__first_"^^f"__begin_"^^f"__end_"^^f""{?="__cap_"^^f}}"__start_"Q""{?="__size_"Q}} _x;
{deque<float, std::allocator<float>>="__map_"{__split_buffer<float *, std::allocator<float *>>="__first_"^^f"__begin_"^^f"__end_"^^f""{?="__cap_"^^f}}"__start_"Q""{?="__size_"Q}} _y;
```

## Instance methods

```
-[PolyNomialExtrapolation ready];
-[PolyNomialExtrapolation predict];
-[PolyNomialExtrapolation initWithHistorySize:degreeOfPolynomial:];
-[PolyNomialExtrapolation printHistoryNamed:];
-[PolyNomialExtrapolation pushPoint:];
```
