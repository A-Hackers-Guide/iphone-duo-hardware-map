# `_UIFastIndexSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{variant<_UIBitSet<256>, _UISmallVector<unsigned short, 16>, std::vector<unsigned long>>="__impl_"{__impl<_UIBitSet<256>, _UISmallVector<unsigned short, 16>, std::vector<unsigned long>>="__data"(__union<std::__variant_detail::_Trait::_Available, 0UL, _UIBitSet<256>, _UISmallVector<unsigned short, 16>, std::vector<unsigned long>>="__dummy"c"__head"{__alt<0UL, _UIBitSet<256>>="__value"{_UIBitSet<256UL>="_chunks"[4Q]}}"__tail"(__union<std::__variant_detail::_Trait::_Available, 1UL, _UISmallVector<unsigned short, 16>, std::vector<unsigned long>>="__dummy"c"__head"{__alt<1UL, _UISmallVector<unsigned short, 16>>="__value"{_UISmallVector<unsigned short, 16UL>="_vector""_size"Q}}"__tail"(__union<std::__variant_detail::_Trait::_Available, 2UL, std::vector<unsigned long>>="__dummy"c"__head"{__alt<2UL, std::vector<unsigned long>>="__value"{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}}}"__tail"(__union<std::__variant_detail::_Trait::_Available, 3UL>=))))"__index"I}} _inOutIndexes;
```

## Class methods

```
+[_UIFastIndexSet indexSet];
```

## Instance methods

```
-[_UIFastIndexSet mutableCopyWithZone:];
-[_UIFastIndexSet hash];
-[_UIFastIndexSet description];
-[_UIFastIndexSet copyWithZone:];
-[_UIFastIndexSet isEqual:];
```
