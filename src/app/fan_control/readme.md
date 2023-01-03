# Fan Control Module


## Summary

A controller for a fan attached to a piece of manufacturing equipment that should:

1) Turn on automatically when the equipment gets too hot
2) Be able to be controlled by a toggle button also

A warning light should come on above a higher threshold. An alarm with reset should trigger above a third threshold.

## Specification

### Fan Control Module
- Read the temperature probe every second
- If temperature > 70 C: start fan
- Button should toggle the fan on and off

### Out of Scope
- temp > 80C: light up warning LED
- warning should turn off automatically
- temp > 90C: sound alarm (flash two LEDs in a pattern)
- alarm should NOT turn off automatically
- alarm should be resetable with a button


## Implementation Details

