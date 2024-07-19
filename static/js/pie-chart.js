 // end am5.ready()

function loadGraphic(id, vitorias, derrotas) {
    var root = am5.Root.new(id);
    root.setThemes([
      am5themes_Animated.new(root)
    ]);
    var chart = root.container.children.push(am5percent.PieChart.new(root, {
      layout: root.verticalLayout
    }));
    
    var series = chart.series.push(am5percent.PieSeries.new(root, {
      valueField: "value",
      categoryField: "category"
    }));

    series.slices.template.setAll({
        fillOpacity: 1,
        stroke: am5.color(0x000000),
        strokeWidth: 1
    });

    series.get("colors").set("colors", [
        am5.color(0xa02a89),
        am5.color(0x6a1c71),
    ]);
    series.slices.template.set("toggleKey", "none");
    series.ticks.template.set("visible", false);
    series.labels.template.set("forceHidden", true);
    
    // Set data
    series.data.setAll([
        { 
            value: +vitorias, 
            category: "Vitórias" ,
            sliceSettings: {
                fill: am5.color(0xffffff),
            }
        }, { 
            value: +derrotas, 
            category: "Derrotas",
            sliceSettings: {
                fill: am5.color(0xffffff),
            }
        }
    ]);

    series.appear(1000, 100);
}

function createChart(id, vitorias, derrotas) {
    var root2 = am5.Root.new(id);
    root2.setThemes([am5themes_Animated.new(root2)]);

    var chart = root2.container.children.push(am5percent.PieChart.new(root2, {
        layout: root2.verticalLayout
    }));

    var series = chart.series.push(am5percent.PieSeries.new(root2, {
        valueField: "value",
        categoryField: "category"
    }));

    series.slices.template.setAll({
        fillOpacity: 1,
        stroke: am5.color(0x000000),
        strokeWidth: 1
    });

    series.get("colors").set("colors", [
        am5.color(0xa02a89),
        am5.color(0x6a1c71),
    ]);
    series.slices.template.set("toggleKey", "none");
    series.ticks.template.set("visible", false);
    series.labels.template.set("forceHidden", true);

    series.data.setAll([
        { 
            value: +vitorias, 
            category: "Vitórias" ,
            sliceSettings: {
                fill: am5.color(0xffffff),
            }
        }, { 
            value: +derrotas, 
            category: "Derrotas",
            sliceSettings: {
                fill: am5.color(0xffffff),
            }
        }
    ]);

    series.appear(1000, 100);
}