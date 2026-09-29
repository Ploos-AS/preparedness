# Batteries, Inverter and Solar

Batteries are quiet and produce no exhaust at the point of use. This makes them particularly attractive in flats and for small to medium loads.

## Nominal capacity is the starting point

A 12 V, 100 Ah battery represents nominally:

`12 V × 100 Ah = 1200 Wh`

That does **not** mean 1200 Wh will necessarily reach a 230 V appliance. Usable capacity depends on factors including battery chemistry, permitted depth of discharge, temperature, age and conversion losses.

Keep two values in the plan:

- **nominal energy**
- **planned usable energy**

Make the assumption between them explicit.

## Inverter

An inverter converts DC to AC. It must be able to support the continuous load, any necessary starting or peak load, and the characteristics of the connected equipment.

A 2000 W inverter does not turn a 1200 Wh battery into a 2000 Wh battery. Power capacity and energy capacity are different quantities.

## Example: 500 Wh usable energy

If the system has already been established to provide **500 Wh of usable energy**, idealised runtime is:

- 10 W load → 50 hours
- 50 W load → 10 hours
- 100 W load → 5 hours
- 500 W load → 1 hour

These are arithmetic examples, not promises of real runtime. Actual loads, temperature and system losses belong in the plan.

## Portable power station

A portable power station typically combines a battery, charger, controls and several outputs. Evaluate it by usable Wh, DC and USB outputs, continuous AC power, peak capability, charging time, supported charging sources, temperature limits and whether the battery can be maintained or replaced.

Do not choose one from its advertised watt figure alone.

## Solar

Solar panels can replenish a battery and extend endurance, but production is variable.

Distinguish between:

- panel rated watts
- actual energy harvested in Wh per day
- charging and conversion losses
- season
- weather
- orientation and shading

Across Europe, latitude and season matter greatly. A northern-European winter plan must not be sized from optimistic summer production.

## Hybrid plan

For a house, a useful architecture can be:

**battery → quiet continuous small loads → generator during limited periods → battery charging + selected large loads**

The generator does not then necessarily need to run continuously.

In a flat, a battery or power station is often much more practical than combustion-based generation, but the energy budget must consequently be stricter.

## Keep operating modes

Define at least three modes: normal preparedness operation, conservation and minimum operation. Decide which loads disappear at each step before the battery is nearly empty.

Reserve energy for the functions that matter most rather than treating every available watt-hour as immediately spendable.

## Measure the real system

For each critical load record measured or documented watts, hours per day, duty cycle where relevant, starting watts and whether AC conversion is required.

Then test the complete path you intend to use: charger, battery, inverter or DC output, cable and appliance. Real preparedness capacity is the capacity the system can deliver safely and repeatably, not merely the number printed on one component.
