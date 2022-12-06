class AcGamePlayground{
    constructor(root){
        this.root = root;
        this.$playground = $(`
<div class="ac-game-playground"></div>
`);
        this.hide();

        this.root.$ac_game.append(this.$playground);
        this.width = this.$playground.width();
        this.height = this.$playground.height();
        this.game_map = new GameMap(this);
        this.players = [];
        this.players.push(new Player(this, this.width / 2, this.height / 2, this.height * 0.05, "white", this.height * 0.25, true));

        for(let i = 0; i < 7; i++){
            this.players.push(new Player(this, this.width / 2, this.height / 2, this.height * 0.05, this.get_random_color(), this.height * 0.15, false));
        }

        this.start();
    }

    get_random_color(){
        let colors = ["green", "DeepSkyBlue", "red", "gold", "grey", "purple", "Sienna"];
        return colors[Math.floor(Math.random() * 7)];
    }

    start(){
    }

    show(){ //打开playground界面
        this.$playground.show();
    }

    hide(){ //关闭playground界面
        this.$playground.hide();
    }
}
